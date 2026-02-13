import trimesh
import numpy as np

def create_human_jointed(scene, pos, rot_y=0, name_prefix='human'):
    SKIN = [255, 206, 180, 255]
    CLOTHES_TOP = [70, 130, 180, 255]
    CLOTHES_BOTTOM = [40, 40, 40, 255]
    HAIR = [50, 30, 10, 255]

    # Use a container node to hold the whole human
    # Actually trimesh scene adds geometries at specific transforms.
    # To animate in Three.js, we want the hierarchy.
    # Trimesh scene.graph can do this.

    # Root node for human
    human_root = trimesh.creation.uv_sphere(radius=0.01) # dummy
    human_root.visual.face_colors = [0,0,0,0]
    base_trans = trimesh.transformations.translation_matrix(pos)
    base_rot = trimesh.transformations.rotation_matrix(rot_y, [0, 1, 0])
    root_transform = np.dot(base_trans, base_rot)

    scene.add_geometry(human_root, transform=root_transform, node_name=f'{name_prefix}_root')

    # Torso (Parent for head and arms)
    torso = trimesh.creation.box(extents=[0.3, 0.5, 0.15])
    torso.visual.face_colors = CLOTHES_TOP
    torso_trans = trimesh.transformations.translation_matrix([0, 0.65, 0])
    scene.add_geometry(torso, transform=torso_trans, node_name=f'{name_prefix}_torso', parent_node_name=f'{name_prefix}_root')

    # Head
    head = trimesh.creation.uv_sphere(radius=0.1)
    head.visual.face_colors = SKIN
    head_trans = trimesh.transformations.translation_matrix([0, 0.35, 0])
    scene.add_geometry(head, transform=head_trans, node_name=f'{name_prefix}_head', parent_node_name=f'{name_prefix}_torso')

    # Hair
    hair = trimesh.creation.uv_sphere(radius=0.105)
    hair.visual.face_colors = HAIR
    scene.add_geometry(hair, transform=trimesh.transformations.translation_matrix([0, 0.02, -0.02]), node_name=f'{name_prefix}_hair', parent_node_name=f'{name_prefix}_head')

    # Arms
    for side, x in [('l', -0.18), ('r', 0.18)]:
        # Upper Arm
        u_arm = trimesh.creation.cylinder(radius=0.04, height=0.25)
        u_arm.visual.face_colors = CLOTHES_TOP
        u_trans = trimesh.transformations.translation_matrix([x, 0.15, 0])
        scene.add_geometry(u_arm, transform=u_trans, node_name=f'{name_prefix}_arm_{side}_u', parent_node_name=f'{name_prefix}_torso')

        # Lower Arm
        l_arm = trimesh.creation.cylinder(radius=0.035, height=0.25)
        l_arm.visual.face_colors = SKIN
        l_trans = trimesh.transformations.translation_matrix([0, -0.2, 0]) # relative to upper arm?
        # Trimesh parent_node_name works with world transforms if not careful.
        # Actually in trimesh scene.add_geometry(..., parent_node_name='...')
        # the transform is relative to the parent.
        scene.add_geometry(l_arm, transform=l_trans, node_name=f'{name_prefix}_arm_{side}_l', parent_node_name=f'{name_prefix}_arm_{side}_u')

    # Legs
    for side, x in [('l', -0.1), ('r', 0.1)]:
        # Upper Leg
        u_leg = trimesh.creation.cylinder(radius=0.06, height=0.35)
        u_leg.visual.face_colors = CLOTHES_BOTTOM
        u_trans = trimesh.transformations.translation_matrix([x, 0.25, 0])
        scene.add_geometry(u_leg, transform=u_trans, node_name=f'{name_prefix}_leg_{side}_u', parent_node_name=f'{name_prefix}_root')

        # Lower Leg
        l_leg = trimesh.creation.cylinder(radius=0.05, height=0.35)
        l_leg.visual.face_colors = CLOTHES_BOTTOM
        l_trans = trimesh.transformations.translation_matrix([0, -0.35, 0])
        scene.add_geometry(l_leg, transform=l_trans, node_name=f'{name_prefix}_leg_{side}_l', parent_node_name=f'{name_prefix}_leg_{side}_u')

def create_miniature_room():
    scene = trimesh.Scene()

    # Colors
    WALL_COLOR = [245, 245, 240, 255]
    FLOOR_COLOR = [220, 220, 210, 255]
    WOOD_DARK = [70, 45, 30, 255]
    WOOD_LIGHT = [160, 120, 90, 255]
    METAL = [150, 150, 160, 255]
    BED_FABRIC = [240, 240, 245, 255]
    MOTHER_GREEN = [46, 139, 87, 255]

    # Room Base (Miniature look - open walls)
    base = trimesh.creation.box(extents=[4, 0.1, 4])
    base.visual.face_colors = FLOOR_COLOR
    scene.add_geometry(base, transform=trimesh.transformations.translation_matrix([0, -0.05, 0]), node_name='floor')

    # Back Wall (Partial)
    wall_back = trimesh.creation.box(extents=[4, 2.5, 0.1])
    wall_back.visual.face_colors = WALL_COLOR
    scene.add_geometry(wall_back, transform=trimesh.transformations.translation_matrix([0, 1.25, -2]), node_name='wall_back')

    # Left Wall (Partial)
    wall_left = trimesh.creation.box(extents=[0.1, 2.5, 2])
    wall_left.visual.face_colors = WALL_COLOR
    scene.add_geometry(wall_left, transform=trimesh.transformations.translation_matrix([-2, 1.25, -1]), node_name='wall_left')

    # Bed (Premium Furnished)
    bed_frame = trimesh.creation.box(extents=[1.2, 0.3, 2.0])
    bed_frame.visual.face_colors = WOOD_DARK
    scene.add_geometry(bed_frame, transform=trimesh.transformations.translation_matrix([-1.0, 0.15, 0.5]), node_name='bed_base')

    bed_linen = trimesh.creation.box(extents=[1.22, 0.15, 2.02])
    bed_linen.visual.face_colors = BED_FABRIC
    scene.add_geometry(bed_linen, transform=trimesh.transformations.translation_matrix([-1.0, 0.35, 0.5]), node_name='bed_linen')

    pillow = trimesh.creation.box(extents=[0.6, 0.1, 0.4])
    pillow.visual.face_colors = [255, 255, 255, 255]
    scene.add_geometry(pillow, transform=trimesh.transformations.translation_matrix([-1.0, 0.45, -0.2]), node_name='pillow')

    # Wardrobe (Wooden texture)
    wardrobe = trimesh.creation.box(extents=[1.0, 2.0, 0.6])
    wardrobe.visual.face_colors = WOOD_DARK
    scene.add_geometry(wardrobe, transform=trimesh.transformations.translation_matrix([-1.4, 1.0, -1.6]), node_name='wooden_wardrobe')

    # Study Desk (Metal frame)
    desk_top = trimesh.creation.box(extents=[1.2, 0.05, 0.6])
    desk_top.visual.face_colors = WOOD_LIGHT
    scene.add_geometry(desk_top, transform=trimesh.transformations.translation_matrix([1.2, 0.75, -1.0]), node_name='study_desk')

    for x, z in [ (0.65, -0.75), (1.75, -0.75), (0.65, -1.25), (1.75, -1.25) ]:
        leg = trimesh.creation.cylinder(radius=0.02, height=0.75)
        leg.visual.face_colors = METAL
        scene.add_geometry(leg, transform=trimesh.transformations.translation_matrix([x, 0.375, z]), node_name=f'desk_leg_{x}_{z}')

    # Laptop
    laptop = trimesh.creation.box(extents=[0.4, 0.02, 0.3])
    laptop.visual.face_colors = [50, 50, 50, 255]
    scene.add_geometry(laptop, transform=trimesh.transformations.translation_matrix([1.2, 0.78, -1.0]), node_name='laptop')

    # Meal Plate
    plate = trimesh.creation.cylinder(radius=0.1, height=0.02)
    plate.visual.face_colors = [240, 240, 240, 255]
    scene.add_geometry(plate, transform=trimesh.transformations.translation_matrix([0.8, 0.78, -1.0]), node_name='meal_plate')

    # WiFi Router
    router = trimesh.creation.box(extents=[0.15, 0.03, 0.12])
    router.visual.face_colors = [20, 20, 20, 255]
    scene.add_geometry(router, transform=trimesh.transformations.translation_matrix([1.7, 0.78, -1.2]), node_name='wifi_router')

    led = trimesh.creation.uv_sphere(radius=0.01)
    led.visual.face_colors = [100, 255, 100, 255]
    scene.add_geometry(led, transform=trimesh.transformations.translation_matrix([1.75, 0.8, -1.15]), node_name='wifi_led')

    # CCTV
    cctv = trimesh.creation.uv_sphere(radius=0.08)
    cctv.visual.face_colors = [220, 220, 220, 255]
    scene.add_geometry(cctv, transform=trimesh.transformations.translation_matrix([1.8, 2.3, -1.8]), node_name='cctv_camera')

    # Split AC
    ac = trimesh.creation.box(extents=[0.8, 0.25, 0.2])
    ac.visual.face_colors = [250, 250, 250, 255]
    scene.add_geometry(ac, transform=trimesh.transformations.translation_matrix([0, 2.1, -1.9]), node_name='ac_unit')

    # Water Purifier
    purifier = trimesh.creation.cylinder(radius=0.08, height=0.25)
    purifier.visual.face_colors = [200, 230, 255, 180]
    scene.add_geometry(purifier, transform=trimesh.transformations.translation_matrix([1.7, 0.9, -0.8]), node_name='water_purifier')

    glass = trimesh.creation.cylinder(radius=0.03, height=0.1)
    glass.visual.face_colors = [200, 230, 255, 100]
    scene.add_geometry(glass, transform=trimesh.transformations.translation_matrix([1.6, 0.83, -0.8]), node_name='water_glass')

    # UPS Unit
    ups = trimesh.creation.box(extents=[0.2, 0.3, 0.4])
    ups.visual.face_colors = [30, 30, 30, 255]
    scene.add_geometry(ups, transform=trimesh.transformations.translation_matrix([1.7, 0.15, -1.2]), node_name='ups_unit')

    # Laundry Basket
    basket = trimesh.creation.cylinder(radius=0.2, height=0.4)
    basket.visual.face_colors = [150, 120, 100, 255]
    scene.add_geometry(basket, transform=trimesh.transformations.translation_matrix([-1.6, 0.2, 1.6]), node_name='laundry_basket')

    # Cleaning Tools
    broom_handle = trimesh.creation.cylinder(radius=0.015, height=1.2)
    broom_handle.visual.face_colors = WOOD_LIGHT
    scene.add_geometry(broom_handle, transform=trimesh.transformations.translation_matrix([-1.8, 0.6, -1.8]), node_name='cleaning_broom')

    broom_head = trimesh.creation.box(extents=[0.2, 0.1, 0.05])
    broom_head.visual.face_colors = [200, 180, 50, 255]
    scene.add_geometry(broom_head, transform=trimesh.transformations.translation_matrix([-1.8, 0.05, -1.8]), node_name='broom_head')

    # Human
    create_human_jointed(scene, [1.1, 0.05, -0.8], rot_y=0, name_prefix='human')

    # Export
    scene.export('mother-homes-viewer/public/models/room.glb')
    print("room.glb generated for React app.")

if __name__ == '__main__':
    import os
    os.makedirs('mother-homes-viewer/public/models', exist_ok=True)
    create_miniature_room()
