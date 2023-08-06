import os

import maya.OpenMaya as om
import maya.cmds as cmds


class CustomObjectBase(object):
    def __init__(self):
        # 储存所有属性的字典
        self.__custom_properties = {}
        # 储存所有信息的字典
        self.__custom_data = {}

    def add_property_to_custom_properties(self, d1):
        self.__custom_properties = {**self.__custom_properties, **d1}

    def get_custom_properties(self):
        return self.__custom_properties


class CustomObject(CustomObjectBase):
    def __init__(self):
        super().__init__()


class CustomScene(CustomObject):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.__file_path = ''
        self.__full_path = os.path.normpath(self.__file_path)
        self.__scene_type = ''

    def __update_data(self):

        self.add_property_to_custom_properties(
            {
                'SceneName': self.get_scene_name(),
                'FullPath': self.get_file_path(),
            }
        )
        print('更新数据中。。。')
        print(self.get_custom_properties())

    def is_maya_file(self):
        """
        如果是Maya类型的文件，则返回后缀名。如果不是，则返回False或这None
        :return:
        """
        if os.path.isfile(self.get_file_path()):
            _, suffix = os.path.splitext(os.path.basename(self.__full_path))
            if suffix in ['.ma', '.mb']:
                return suffix
        return False

    def get_scene_name(self):
        scene_name, _ = os.path.splitext(os.path.basename(os.path.normpath(self.get_file_path())))
        return scene_name

    def get_file_path(self):
        return self.__file_path

    def set_file_path(self, file_path):
        print('设定文件路径')
        if not self.is_maya_file:
            raise Exception(f'>>{str(file_path)}<< is not a legal address!')
        else:
            self.__file_path = file_path

        self.__update_data()


class SceneDetails(CustomScene):
    def __init__(self, *args, **kwargs):
        super().__init__()

    def get_scene_evaluate(self):
        return {
            **self.get_poly_evaluate(),
            **self.get_joint_evaluate(),
            **{
                'HasSameTransform': self.has_same_name_transform(),
                'HasSameJoint': self.has_same_name_joint(),
            },
            **self.get_blendshape_evaluate(),
        }

    def get_poly_evaluate(self):
        __meshes = cmds.ls(type='mesh')
        return {
            'Verts': cmds.polyEvaluate(__meshes, vertex=True) if len(__meshes) > 0 else 0,
            'Edges': cmds.polyEvaluate(__meshes, edge=True) if len(__meshes) > 0 else 0,
            'Faces': cmds.polyEvaluate(__meshes, face=True) if len(__meshes) > 0 else 0,
            'Tris': cmds.polyEvaluate(__meshes, triangle=True) if len(__meshes) > 0 else 0,
            'UVs': cmds.polyEvaluate(__meshes, uv=True) if len(__meshes) > 0 else 0,
            'Ngons': len(self.get_objects_with_more_than_4_sides_long_list())
        }

    def get_objects_with_more_than_4_sides_long_list(self):
        cmds.select(cmds.ls(type='mesh'))
        sel = om.MSelectionList()
        om.MGlobal.getActiveSelectionList(sel)
        poly_objects = []

        for i in range(sel.length()):
            m_obj = om.MObject()
            sel.getDependNode(i, m_obj)

            if m_obj.hasFn(om.MFn.kMesh):
                dag_path = om.MDagPath()
                sel.getDagPath(i, dag_path)
                poly = om.MFnMesh(dag_path)

                for j in range(poly.numPolygons()):
                    vertices = om.MIntArray()
                    poly.getPolygonVertices(j, vertices)

                    if len(vertices) > 4:
                        poly_objects.append(dag_path.fullPathName())
                        break
        cmds.select(cl=True)
        return poly_objects

    def get_joint_evaluate(self):
        return {
            'Joints': len(cmds.ls(type='joint'))
        }

    def get_blendshape_evaluate(self):
        blend_shapes = cmds.ls(type='blendShape')
        morph_target_counter = 0
        for bs in blend_shapes:
            morph_target_counter += cmds.blendShape(bs, query=True, weightCount=True)
        return {
            'BlendShapes': len(blend_shapes),
            'MorphTargets': morph_target_counter
        }

    @staticmethod
    def has_same_name_joint():
        for i in cmds.ls(type='joint'):
            if '|' in i:
                return True
        return False

    @staticmethod
    def has_same_name_transform():
        for i in cmds.ls(type='transform'):
            if '|' in i:
                return True
        return False

    def func(self):
        pass
