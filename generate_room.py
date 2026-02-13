import trimesh
import numpy as np

def create_human(scene, pos, rot_y=0, state='sitting', name_prefix='human'):
    SKIN = [255, 206, 180, 255]
    CLOTHES_TOP = [70, 130, 180, 255]
    CLOTHES_BOTTOM = [40, 40, 40, 255]
    HAIR = [50, 30, 10, 255]

    head_r = 0.1
    neck_h = 0.05
    torso_h = 0.5
    thigh_h = 0.4
    u_arm_h = 0.3

    base_t = trimesh.transformations.translation_matrix(pos)
    base_r = trimesh.transformations.rotation_matrix(rot_y, [0, 1, 0])
    world = np.dot(base_t, base_r)

    def add(geom, local_trans, name=None):
        m = np.dot(world, local_trans)
        scene.add_geometry(geom, transform=m, node_name=name)

    if state == 'sitting':
        y_hip = 0.45

        # Torso
        torso = trimesh.creation.box(extents=[0.35, torso_h, 0.18])
        torso.visual.face_colors = CLOTHES_TOP
        add(torso, trimesh.transformations.translation_matrix([0, y_hip + 0.25, 0]), name=f'{name_prefix}_torso')

        # Thighs (forward)
        for x in [-0.1, 0.1]:
            thigh = trimesh.creation.cylinder(radius=0.07, height=thigh_h)
            thigh.visual.face_colors = CLOTHES_BOTTOM
            rot = trimesh.transformations.rotation_matrix(np.pi/2, [1, 0, 0])
            trans = trimesh.transformations.translation_matrix([x, y_hip, 0.2])
            add(thigh, np.dot(trans, rot))

            knee = trimesh.creation.uv_sphere(radius=0.07)
            knee.visual.face_colors = CLOTHES_BOTTOM
            add(knee, trimesh.transformations.translation_matrix([x, y_hip, 0.4]))

            calf = trimesh.creation.cylinder(radius=0.06, height=y_hip)
            calf.visual.face_colors = CLOTHES_BOTTOM
            add(calf, trimesh.transformations.translation_matrix([x, y_hip/2, 0.4]))

        # Shoulders and Arms (towards desk)
        y_sh = y_hip + 0.45
        for x in [-0.18, 0.18]:
            sh = trimesh.creation.uv_sphere(radius=0.06)
            sh.visual.face_colors = CLOTHES_TOP
            add(sh, trimesh.transformations.translation_matrix([x, y_sh, 0]))

            # Upper arm (diagonal)
            u_arm = trimesh.creation.cylinder(radius=0.04, height=u_arm_h)
            u_arm.visual.face_colors = CLOTHES_TOP
            rot = trimesh.transformations.rotation_matrix(np.pi/4, [1, 0, 0])
            trans = trimesh.transformations.translation_matrix([x, y_sh - 0.1, 0.1])
            add(u_arm, np.dot(trans, rot))

            # Lower arm (forward)
            l_arm = trimesh.creation.cylinder(radius=0.035, height=0.25)
            l_arm.visual.face_colors = SKIN
            rot = trimesh.transformations.rotation_matrix(np.pi/2, [1, 0, 0])
            trans = trimesh.transformations.translation_matrix([x, y_sh - 0.15, 0.3])
            add(l_arm, np.dot(trans, rot))

        # Neck & Head
        h_y = y_hip + torso_h + neck_h + head_r
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

def create_room():
    scene = trimesh.Scene()

    WALL = [240, 240, 240, 255]
    FLOOR = [140, 140, 140, 255]
    WOOD = [80, 50, 30, 255] # Darker wood
    BED_LINEN = [245, 245, 245, 255]
    BLACK = [30, 30, 30, 255]
    GLASS = [200, 230, 255, 150]
    ROUTER_GLOW = [100, 255, 100, 255]
    PURPLE = [120, 40, 180, 255] # Purple for bean bag
    MOTHER_GREEN = [46, 139, 87, 255]

    # Floor and Walls
    floor = trimesh.creation.box(extents=[4, 0.1, 4])
    floor.visual.face_colors = FLOOR
    scene.add_geometry(floor, transform=trimesh.transformations.translation_matrix([0, -0.05, 0]))

    wall_back = trimesh.creation.box(extents=[4, 2.5, 0.1])
    wall_back.visual.face_colors = WALL
    scene.add_geometry(wall_back, transform=trimesh.transformations.translation_matrix([0, 1.25, -2]), node_name='wall_back')

    wall_left = trimesh.creation.box(extents=[0.1, 2.5, 4])
    wall_left.visual.face_colors = WALL
    scene.add_geometry(wall_left, transform=trimesh.transformations.translation_matrix([-2, 1.25, 0]), node_name='wall_left')

    wall_right = trimesh.creation.box(extents=[0.1, 2.5, 4])
    wall_right.visual.face_colors = WALL
    scene.add_geometry(wall_right, transform=trimesh.transformations.translation_matrix([2, 1.25, 0]), node_name='wall_right')

    # Window on the right wall
    window_frame = trimesh.creation.box(extents=[0.12, 1.2, 1.5])
    window_frame.visual.face_colors = [100, 100, 100, 255]
    scene.add_geometry(window_frame, transform=trimesh.transformations.translation_matrix([2.0, 1.3, 0.5]), node_name='window_frame')

    window_glass = trimesh.creation.box(extents=[0.02, 1.1, 1.4])
    window_glass.visual.face_colors = GLASS
    scene.add_geometry(window_glass, transform=trimesh.transformations.translation_matrix([2.0, 1.3, 0.5]), node_name='window_glass')

    # Branding
    brand_bg = trimesh.creation.box(extents=[0.6, 0.3, 0.02])
    brand_bg.visual.face_colors = [255, 255, 255, 255]
    scene.add_geometry(brand_bg, transform=trimesh.transformations.translation_matrix([0, 1.8, -1.94]), node_name='branding_bg')

    brand_logo = trimesh.creation.box(extents=[0.1, 0.1, 0.03])
    brand_logo.visual.face_colors = MOTHER_GREEN
    scene.add_geometry(brand_logo, transform=trimesh.transformations.translation_matrix([-0.2, 1.8, -1.93]), node_name='branding_logo')

    # Bed
    bed_base = trimesh.creation.box(extents=[1.2, 0.4, 2.0])
    bed_base.visual.face_colors = WOOD
    scene.add_geometry(bed_base, transform=trimesh.transformations.translation_matrix([-0.2, 0.2, -0.5]), node_name='bed_base')

    linen = trimesh.creation.box(extents=[1.22, 0.1, 2.02])
    linen.visual.face_colors = BED_LINEN
    scene.add_geometry(linen, transform=trimesh.transformations.translation_matrix([-0.2, 0.45, -0.5]), node_name='bed_linen')

    towel = trimesh.creation.box(extents=[0.4, 0.05, 0.3])
    towel.visual.face_colors = [200, 200, 255, 255]
    scene.add_geometry(towel, transform=trimesh.transformations.translation_matrix([-0.2, 0.52, 0.2]), node_name='folded_towels')

    # Side table
    side_table = trimesh.creation.box(extents=[0.4, 0.4, 0.4])
    side_table.visual.face_colors = WOOD
    scene.add_geometry(side_table, transform=trimesh.transformations.translation_matrix([-1.0, 0.2, -1.0]), node_name='side_table')

    router = trimesh.creation.box(extents=[0.15, 0.03, 0.12])
    router.visual.face_colors = BLACK
    scene.add_geometry(router, transform=trimesh.transformations.translation_matrix([-1.0, 0.415, -1.0]), node_name='wifi_router')
    glow = trimesh.creation.uv_sphere(radius=0.01)
    glow.visual.face_colors = ROUTER_GLOW
    scene.add_geometry(glow, transform=trimesh.transformations.translation_matrix([-0.95, 0.43, -0.95]))

    purifier = trimesh.creation.cylinder(radius=0.08, height=0.2)
    purifier.visual.face_colors = GLASS
    scene.add_geometry(purifier, transform=trimesh.transformations.translation_matrix([-1.0, 0.5, -1.15]), node_name='water_purifier')

    # Desk
    desk = trimesh.creation.box(extents=[1.2, 0.05, 0.6])
    desk.visual.face_colors = WOOD
    scene.add_geometry(desk, transform=trimesh.transformations.translation_matrix([1.2, 0.75, -1.4]), node_name='study_desk')

    laptop = trimesh.creation.box(extents=[0.4, 0.02, 0.3])
    laptop.visual.face_colors = [50, 50, 50, 255]
    scene.add_geometry(laptop, transform=trimesh.transformations.translation_matrix([0.8, 0.78, -1.3]), node_name='laptop')

    # Dining accessories
    plate = trimesh.creation.cylinder(radius=0.12, height=0.02)
    plate.visual.face_colors = [255, 255, 255, 255]
    scene.add_geometry(plate, transform=trimesh.transformations.translation_matrix([1.4, 0.78, -1.3]), node_name='dining_plate')

    fork = trimesh.creation.box(extents=[0.01, 0.005, 0.15])
    fork.visual.face_colors = [180, 180, 180, 255]
    scene.add_geometry(fork, transform=trimesh.transformations.translation_matrix([1.25, 0.78, -1.3]))

    knife = trimesh.creation.box(extents=[0.01, 0.005, 0.15])
    knife.visual.face_colors = [180, 180, 180, 255]
    scene.add_geometry(knife, transform=trimesh.transformations.translation_matrix([1.55, 0.78, -1.3]))

    ups = trimesh.creation.box(extents=[0.2, 0.3, 0.4])
    ups.visual.face_colors = BLACK
    scene.add_geometry(ups, transform=trimesh.transformations.translation_matrix([1.5, 0.15, -1.4]), node_name='ups_unit')

    chair = trimesh.creation.box(extents=[0.5, 0.05, 0.5])
    chair.visual.face_colors = BLACK
    scene.add_geometry(chair, transform=trimesh.transformations.translation_matrix([1.1, 0.45, -0.8]), node_name='study_chair')

    create_human(scene, [1.1, 0.05, -0.85], rot_y=0, state='sitting', name_prefix='room_human')

    # Wardrobe
    wardrobe = trimesh.creation.box(extents=[0.8, 1.8, 0.6])
    wardrobe.visual.face_colors = WOOD
    scene.add_geometry(wardrobe, transform=trimesh.transformations.translation_matrix([-1.5, 0.9, 0.5]), node_name='wooden_wardrobe')

    laundry = trimesh.creation.cylinder(radius=0.2, height=0.4)
    laundry.visual.face_colors = [150, 120, 100, 255]
    scene.add_geometry(laundry, transform=trimesh.transformations.translation_matrix([-1.5, 0.2, 1.2]), node_name='laundry_basket')

    vacuum = trimesh.creation.box(extents=[0.2, 0.5, 0.2])
    vacuum.visual.face_colors = [50, 50, 50, 255]
    scene.add_geometry(vacuum, transform=trimesh.transformations.translation_matrix([-1.8, 0.25, -1.8]), node_name='vacuum_cleaner')

    ac = trimesh.creation.box(extents=[0.8, 0.25, 0.2])
    ac.visual.face_colors = [250, 250, 250, 255]
    scene.add_geometry(ac, transform=trimesh.transformations.translation_matrix([0.5, 2.1, -1.9]), node_name='ac_unit')

    # Bean bag
    bean_bag = trimesh.creation.uv_sphere(radius=0.4)
    bean_bag.visual.face_colors = PURPLE
    scene.add_geometry(bean_bag, transform=trimesh.transformations.translation_matrix([1.0, 0.3, 1.2]), node_name='bean_bag')

    cctv = trimesh.creation.uv_sphere(radius=0.1) # Bigger as in image
    cctv.visual.face_colors = [230, 230, 230, 255]
    scene.add_geometry(cctv, transform=trimesh.transformations.translation_matrix([1.8, 2.3, -1.8]), node_name='cctv_camera')

    tube_light = trimesh.creation.cylinder(radius=0.02, height=1.2)
    tube_light.visual.face_colors = [255, 255, 255, 255]
    rot = trimesh.transformations.rotation_matrix(np.pi/2, [0, 0, 1])
    trans = trimesh.transformations.translation_matrix([0, 2.4, -1.95])
    scene.add_geometry(tube_light, transform=np.dot(trans, rot), node_name='tube_light')

    scene.export('room.glb')
    print("room.glb generated successfully.")

if __name__ == '__main__':
    create_room()
