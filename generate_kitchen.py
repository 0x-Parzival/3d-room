import trimesh
import numpy as np

def create_human(scene, pos, rot_y=0, state='standing', name_prefix='human'):
    SKIN = [255, 206, 180, 255]
    CLOTHES_TOP = [60, 100, 60, 255]
    CLOTHES_BOTTOM = [40, 40, 40, 255]
    HAIR = [50, 30, 10, 255]

    head_r = 0.1
    neck_h = 0.05
    torso_h = 0.5
    thigh_h = 0.4
    calf_h = 0.4
    u_arm_h = 0.3
    l_arm_h = 0.3

    base_t = trimesh.transformations.translation_matrix(pos)
    base_r = trimesh.transformations.rotation_matrix(rot_y, [0, 1, 0])
    world = np.dot(base_t, base_r)

    def add(geom, local_trans, name=None):
        m = np.dot(world, local_trans)
        scene.add_geometry(geom, transform=m, node_name=name)

    if state == 'standing':
        # Legs
        for x in [-0.1, 0.1]:
            calf = trimesh.creation.cylinder(radius=0.05, height=calf_h)
            calf.visual.face_colors = CLOTHES_BOTTOM
            add(calf, trimesh.transformations.translation_matrix([x, 0.2, 0]))

            knee = trimesh.creation.uv_sphere(radius=0.06)
            knee.visual.face_colors = CLOTHES_BOTTOM
            add(knee, trimesh.transformations.translation_matrix([x, 0.4, 0]))

            thigh = trimesh.creation.cylinder(radius=0.07, height=thigh_h)
            thigh.visual.face_colors = CLOTHES_BOTTOM
            add(thigh, trimesh.transformations.translation_matrix([x, 0.6, 0]))

        y_torso_bottom = 0.8
        torso = trimesh.creation.box(extents=[0.35, torso_h, 0.18])
        torso.visual.face_colors = CLOTHES_TOP
        add(torso, trimesh.transformations.translation_matrix([0, y_torso_bottom + 0.25, 0]), name=f'{name_prefix}_torso')

        y_sh = y_torso_bottom + 0.45
        for x in [-0.18, 0.18]:
            sh = trimesh.creation.uv_sphere(radius=0.06)
            sh.visual.face_colors = CLOTHES_TOP
            add(sh, trimesh.transformations.translation_matrix([x, y_sh, 0]))

            u_arm = trimesh.creation.cylinder(radius=0.04, height=u_arm_h)
            u_arm.visual.face_colors = CLOTHES_TOP
            add(u_arm, trimesh.transformations.translation_matrix([x, y_sh - 0.15, 0]))

            el = trimesh.creation.uv_sphere(radius=0.04)
            el.visual.face_colors = SKIN
            add(el, trimesh.transformations.translation_matrix([x, y_sh - 0.3, 0]))

            l_arm = trimesh.creation.cylinder(radius=0.035, height=l_arm_h)
            l_arm.visual.face_colors = SKIN
            add(l_arm, trimesh.transformations.translation_matrix([x, y_sh - 0.45, 0]))

        h_y = y_torso_bottom + torso_h + neck_h + head_r
        head = trimesh.creation.uv_sphere(radius=head_r)
        head.visual.face_colors = SKIN
        add(head, trimesh.transformations.translation_matrix([0, h_y, 0]), name=f'{name_prefix}_head')

        for ex in [-0.03, 0.03]:
            eye = trimesh.creation.uv_sphere(radius=0.01)
            eye.visual.face_colors = [0, 0, 0, 255]
            add(eye, trimesh.transformations.translation_matrix([ex, h_y + 0.02, 0.08]))

        hair = trimesh.creation.uv_sphere(radius=0.105)
        hair.visual.face_colors = HAIR
        add(hair, trimesh.transformations.translation_matrix([0, h_y + 0.02, -0.01]))

def create_kitchen():
    scene = trimesh.Scene()

    WOOD = [80, 50, 30, 255] # Darker wood as in image
    GRANITE = [20, 20, 20, 255] # Sleek black granite
    STAINLESS = [200, 200, 200, 255]
    MOSAIC = [60, 50, 45, 255] # Darker mosaic backsplash
    WHITE = [250, 250, 250, 255]
    RED = [220, 40, 40, 255]
    MOTHER_GREEN = [46, 139, 87, 255]

    scene.add_geometry(trimesh.creation.box(extents=[4, 0.1, 4]), transform=trimesh.transformations.translation_matrix([0, -0.05, 0]))

    back_wall = trimesh.creation.box(extents=[4, 2.7, 0.1])
    back_wall.visual.face_colors = [240, 240, 240, 255]
    scene.add_geometry(back_wall, transform=trimesh.transformations.translation_matrix([0, 1.35, -1.5]), node_name='kitchen_back_wall')

    side_wall = trimesh.creation.box(extents=[0.1, 2.7, 4])
    side_wall.visual.face_colors = [240, 240, 240, 255]
    scene.add_geometry(side_wall, transform=trimesh.transformations.translation_matrix([2, 1.35, 0]))

    # Countertop
    counter = trimesh.creation.box(extents=[3.0, 0.05, 0.6])
    counter.visual.face_colors = GRANITE
    scene.add_geometry(counter, transform=trimesh.transformations.translation_matrix([0, 0.9, -1.2]), node_name='granite_countertop')

    # Backsplash
    backsplash = trimesh.creation.box(extents=[3.0, 0.6, 0.02])
    backsplash.visual.face_colors = MOSAIC
    scene.add_geometry(backsplash, transform=trimesh.transformations.translation_matrix([0, 1.2, -1.48]), node_name='mosaic_backsplash')

    # Branding on backsplash
    brand_bg = trimesh.creation.box(extents=[0.5, 0.2, 0.01])
    brand_bg.visual.face_colors = [255, 255, 255, 255]
    scene.add_geometry(brand_bg, transform=trimesh.transformations.translation_matrix([1.0, 1.35, -1.465]), node_name='branding_bg')

    brand_logo = trimesh.creation.box(extents=[0.08, 0.08, 0.02])
    brand_logo.visual.face_colors = MOTHER_GREEN
    scene.add_geometry(brand_logo, transform=trimesh.transformations.translation_matrix([0.85, 1.35, -1.46]), node_name='branding_logo')

    # Overhead cabinets
    overhead = trimesh.creation.box(extents=[3.0, 0.7, 0.35])
    overhead.visual.face_colors = WOOD
    scene.add_geometry(overhead, transform=trimesh.transformations.translation_matrix([0, 2.1, -1.325]), node_name='overhead_cabinets')

    # Chimney hood
    hood = trimesh.creation.box(extents=[0.7, 0.4, 0.45])
    hood.visual.face_colors = STAINLESS
    scene.add_geometry(hood, transform=trimesh.transformations.translation_matrix([0, 1.7, -1.25]), node_name='chimney_hood')

    pipe = trimesh.creation.cylinder(radius=0.1, height=0.6)
    pipe.visual.face_colors = STAINLESS
    scene.add_geometry(pipe, transform=trimesh.transformations.translation_matrix([0, 2.4, -1.25]), node_name='chimney_pipe')

    # Stove
    stove = trimesh.creation.box(extents=[0.7, 0.08, 0.45])
    stove.visual.face_colors = STAINLESS
    scene.add_geometry(stove, transform=trimesh.transformations.translation_matrix([0, 0.96, -1.2]), node_name='gas_stove')

    for x in [-0.18, 0.18]:
        burner = trimesh.creation.cylinder(radius=0.09, height=0.03)
        burner.visual.face_colors = [30, 30, 30, 255]
        scene.add_geometry(burner, transform=trimesh.transformations.translation_matrix([x, 1.01, -1.2]))

    # Cooking essentials
    for i in range(4):
        bottle = trimesh.creation.cylinder(radius=0.03, height=0.2)
        bottle.visual.face_colors = [210, 180, 50, 160]
        scene.add_geometry(bottle, transform=trimesh.transformations.translation_matrix([-0.7 - i*0.1, 1.0, -1.3]), node_name=f'oil_bottle_{i}')

    # Sink
    basin = trimesh.creation.box(extents=[0.6, 0.1, 0.45])
    basin.visual.face_colors = STAINLESS
    scene.add_geometry(basin, transform=trimesh.transformations.translation_matrix([1.0, 0.85, -1.2]), node_name='sink_basin')

    faucet = trimesh.creation.cylinder(radius=0.02, height=0.25)
    faucet.visual.face_colors = STAINLESS
    scene.add_geometry(faucet, transform=trimesh.transformations.translation_matrix([1.0, 1.0, -1.4]), node_name='modern_faucet')

    # Water purifier
    purifier = trimesh.creation.box(extents=[0.4, 0.6, 0.25])
    purifier.visual.face_colors = WHITE
    scene.add_geometry(purifier, transform=trimesh.transformations.translation_matrix([1.6, 1.8, -1.4]), node_name='water_purifier')

    # Gas cylinder
    cylinder = trimesh.creation.cylinder(radius=0.16, height=0.5)
    cylinder.visual.face_colors = RED
    scene.add_geometry(cylinder, transform=trimesh.transformations.translation_matrix([1.0, 0.25, -1.2]), node_name='gas_cylinder')

    # Lower cabinets/drawers
    lower = trimesh.creation.box(extents=[3.0, 0.85, 0.58])
    lower.visual.face_colors = WOOD
    scene.add_geometry(lower, transform=trimesh.transformations.translation_matrix([0, 0.425, -1.21]), node_name='lower_cabinets')

    create_human(scene, [-0.5, 0, -0.7], rot_y=np.pi/4, state='standing', name_prefix='kitchen_human')

    scene.export('kitchen.glb')
    print("kitchen.glb generated successfully.")

if __name__ == '__main__':
    create_kitchen()
