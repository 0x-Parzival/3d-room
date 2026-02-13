import trimesh
import numpy as np

def create_human(scene, pos, rot_y=0, state='sitting', name_prefix='human'):
    # Colors
    SKIN = [255, 220, 180, 255]
    SHIRT = [50, 100, 200, 255]
    PANTS = [40, 40, 40, 255]
    HAIR = [50, 30, 10, 255]

    # Torso
    torso = trimesh.creation.cylinder(radius=0.15, height=0.45)
    torso.visual.face_colors = SHIRT
    t_pos = [pos[0], pos[1] + 0.6, pos[2]]
    scene.add_geometry(torso, transform=trimesh.transformations.translation_matrix(t_pos), node_name=f'{name_prefix}_torso')

    # Head
    head = trimesh.creation.uv_sphere(radius=0.11)
    head.visual.face_colors = SKIN
    h_pos = [t_pos[0], t_pos[1] + 0.35, t_pos[2]]
    scene.add_geometry(head, transform=trimesh.transformations.translation_matrix(h_pos), node_name=f'{name_prefix}_head')

    # Hair
    hair = trimesh.creation.uv_sphere(radius=0.115)
    hair.visual.face_colors = HAIR
    scene.add_geometry(hair, transform=trimesh.transformations.translation_matrix([h_pos[0], h_pos[1]+0.02, h_pos[2]]))

    if state == 'sitting':
        # Arms (resting on desk/lap)
        for x_off in [-0.2, 0.2]:
            arm = trimesh.creation.cylinder(radius=0.04, height=0.4)
            arm.visual.face_colors = SHIRT
            a_trans = trimesh.transformations.translation_matrix([pos[0] + x_off, pos[1] + 0.6, pos[2] + 0.15])
            rot = trimesh.transformations.rotation_matrix(np.pi/2.5, [1, 0, 0])
            scene.add_geometry(arm, transform=np.dot(a_trans, rot))

        # Thighs
        for x_off in [-0.1, 0.1]:
            thigh = trimesh.creation.cylinder(radius=0.07, height=0.35)
            thigh.visual.face_colors = PANTS
            rot = trimesh.transformations.rotation_matrix(np.pi/2, [1, 0, 0])
            trans = trimesh.transformations.translation_matrix([pos[0] + x_off, pos[1] + 0.4, pos[2] + 0.18])
            scene.add_geometry(thigh, transform=np.dot(trans, rot))
            # Calves
            calf = trimesh.creation.cylinder(radius=0.06, height=0.4)
            calf.visual.face_colors = PANTS
            c_trans = trimesh.transformations.translation_matrix([pos[0] + x_off, pos[1] + 0.2, pos[2] + 0.35])
            scene.add_geometry(calf, transform=c_trans)

def create_room():
    scene = trimesh.Scene()

    # Colors
    WALL = [230, 230, 230, 255]
    FLOOR = [150, 150, 150, 255]
    WOOD = [139, 69, 19, 255]
    BED_LINEN = [245, 245, 245, 255]
    BLACK = [30, 30, 30, 255]
    GLASS = [200, 230, 255, 150]
    ROUTER_GLOW = [100, 255, 100, 255]

    # Floor
    floor = trimesh.creation.box(extents=[4, 0.1, 4])
    floor.visual.face_colors = FLOOR
    scene.add_geometry(floor, transform=trimesh.transformations.translation_matrix([0, -0.05, 0]))

    # Rug
    rug = trimesh.creation.box(extents=[2.5, 0.02, 1.8])
    rug.visual.face_colors = [80, 40, 40, 255]
    scene.add_geometry(rug, transform=trimesh.transformations.translation_matrix([0, 0.01, 0.5]))

    # Walls
    scene.add_geometry(trimesh.creation.box(extents=[4, 2.5, 0.1]), transform=trimesh.transformations.translation_matrix([0, 1.25, -2]))
    scene.add_geometry(trimesh.creation.box(extents=[0.1, 2.5, 4]), transform=trimesh.transformations.translation_matrix([-2, 1.25, 0]))

    # --- BED ---
    bed_base = trimesh.creation.box(extents=[1.2, 0.4, 2.0])
    bed_base.visual.face_colors = WOOD
    scene.add_geometry(bed_base, transform=trimesh.transformations.translation_matrix([-0.2, 0.2, -0.5]))

    # Linen & Towels
    linen = trimesh.creation.box(extents=[1.22, 0.1, 2.02])
    linen.visual.face_colors = BED_LINEN
    scene.add_geometry(linen, transform=trimesh.transformations.translation_matrix([-0.2, 0.45, -0.5]), node_name='bedsheet')

    # Towels (folded)
    towel = trimesh.creation.box(extents=[0.4, 0.05, 0.3])
    towel.visual.face_colors = [200, 200, 255, 255]
    scene.add_geometry(towel, transform=trimesh.transformations.translation_matrix([-0.2, 0.52, 0.2]))

    # More Ruffles
    for i in range(10):
        ruffle = trimesh.creation.box(extents=[0.2, 0.02, 0.1])
        ruffle.visual.face_colors = BED_LINEN
        rand_pos = [-0.2 + np.random.uniform(-0.5, 0.5), 0.51, -0.5 + np.random.uniform(-0.8, 0.8)]
        rand_rot = trimesh.transformations.rotation_matrix(np.random.uniform(0, np.pi), [0, 1, 0])
        scene.add_geometry(ruffle, transform=np.dot(trimesh.transformations.translation_matrix(rand_pos), rand_rot))

    # --- SIDE TABLE & GADGETS ---
    side_table = trimesh.creation.box(extents=[0.4, 0.4, 0.4])
    side_table.visual.face_colors = WOOD
    scene.add_geometry(side_table, transform=trimesh.transformations.translation_matrix([-1.0, 0.2, -1.0]))

    # WiFi Router
    router = trimesh.creation.box(extents=[0.15, 0.03, 0.12])
    router.visual.face_colors = BLACK
    scene.add_geometry(router, transform=trimesh.transformations.translation_matrix([-1.0, 0.415, -1.0]))
    glow = trimesh.creation.uv_sphere(radius=0.01)
    glow.visual.face_colors = ROUTER_GLOW
    scene.add_geometry(glow, transform=trimesh.transformations.translation_matrix([-0.95, 0.43, -0.95]))

    # Glass Water Purifier
    purifier_base = trimesh.creation.cylinder(radius=0.08, height=0.2)
    purifier_base.visual.face_colors = GLASS
    scene.add_geometry(purifier_base, transform=trimesh.transformations.translation_matrix([-1.0, 0.5, -1.15]))

    # --- STUDY DESK & UPS ---
    desk = trimesh.creation.box(extents=[1.2, 0.05, 0.6])
    desk.visual.face_colors = WOOD
    scene.add_geometry(desk, transform=trimesh.transformations.translation_matrix([1.2, 0.75, -1.4]))

    # UPS unit
    ups = trimesh.creation.box(extents=[0.2, 0.3, 0.4])
    ups.visual.face_colors = BLACK
    scene.add_geometry(ups, transform=trimesh.transformations.translation_matrix([1.5, 0.15, -1.4]))

    # Laptop & Books
    laptop = trimesh.creation.box(extents=[0.4, 0.02, 0.3])
    laptop.visual.face_colors = [50, 50, 50, 255]
    scene.add_geometry(laptop, transform=trimesh.transformations.translation_matrix([1.2, 0.78, -1.4]))

    # Ergonomic Chair & Human
    chair = trimesh.creation.box(extents=[0.5, 0.05, 0.5])
    chair.visual.face_colors = BLACK
    scene.add_geometry(chair, transform=trimesh.transformations.translation_matrix([1.1, 0.45, -0.8]))
    create_human(scene, [1.1, 0.05, -0.85], state='sitting', name_prefix='room_human')

    # --- OTHER ITEMS ---
    # Wardrobe
    wardrobe = trimesh.creation.box(extents=[0.8, 1.8, 0.6])
    wardrobe.visual.face_colors = WOOD
    scene.add_geometry(wardrobe, transform=trimesh.transformations.translation_matrix([-1.5, 0.9, 0.5]))

    # Laundry Basket
    laundry = trimesh.creation.cylinder(radius=0.2, height=0.4)
    laundry.visual.face_colors = [150, 120, 100, 255]
    scene.add_geometry(laundry, transform=trimesh.transformations.translation_matrix([-1.5, 0.2, 1.2]), node_name='laundry_basket')

    # Vacuum Cleaner
    vacuum = trimesh.creation.box(extents=[0.2, 0.5, 0.2])
    vacuum.visual.face_colors = [200, 0, 0, 255]
    scene.add_geometry(vacuum, transform=trimesh.transformations.translation_matrix([-1.8, 0.25, -1.8]))

    # AC
    ac = trimesh.creation.box(extents=[0.8, 0.25, 0.2])
    ac.visual.face_colors = [250, 250, 250, 255]
    scene.add_geometry(ac, transform=trimesh.transformations.translation_matrix([0.5, 2.1, -1.9]))

    # Bean Bag
    bean_bag = trimesh.creation.uv_sphere(radius=0.4)
    bean_bag.visual.face_colors = [200, 50, 100, 255]
    scene.add_geometry(bean_bag, transform=trimesh.transformations.translation_matrix([1.0, 0.3, 1.2]), node_name='bean_bag')

    # CCTV
    cctv = trimesh.creation.uv_sphere(radius=0.06)
    cctv.visual.face_colors = BLACK
    scene.add_geometry(cctv, transform=trimesh.transformations.translation_matrix([-1.9, 2.4, -1.9]))

    scene.export('room.glb')
    print("room.glb generated successfully.")

if __name__ == '__main__':
    create_room()
