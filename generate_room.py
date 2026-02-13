import trimesh
import numpy as np

def create_room():
    scene = trimesh.Scene()

    # Colors (RGBA)
    WOOD = [139, 69, 19, 255]
    WOOD_LIGHT = [160, 82, 45, 255]
    WHITE = [255, 255, 255, 255]
    OFF_WHITE = [245, 245, 245, 255]
    DARK_GREY = [50, 50, 50, 255]
    LIGHT_GREY = [220, 220, 220, 255]
    BLUE = [100, 149, 237, 255]
    PINK = [255, 105, 180, 255]
    BLACK = [0, 0, 0, 255]
    METAL = [192, 192, 192, 255]
    PURIFIER_GLASS = [173, 216, 230, 180]
    ROUTER_LIGHT = [0, 255, 0, 255]

    # Floor
    floor = trimesh.creation.box(extents=[4, 0.1, 4])
    floor.visual.face_colors = LIGHT_GREY
    scene.add_geometry(floor, transform=trimesh.transformations.translation_matrix([0, -0.05, 0]))

    # Walls
    wall_back = trimesh.creation.box(extents=[4, 2.7, 0.1])
    wall_back.visual.face_colors = WHITE
    scene.add_geometry(wall_back, transform=trimesh.transformations.translation_matrix([0, 1.35, -2]))

    wall_left = trimesh.creation.box(extents=[0.1, 2.7, 4])
    wall_left.visual.face_colors = BLUE # Accent wall
    scene.add_geometry(wall_left, transform=trimesh.transformations.translation_matrix([-2, 1.35, 0]))

    # --- BED ---
    # Bed frame legs
    for x in [-0.55, 0.55]:
        for z in [-0.95, 0.95]:
            leg = trimesh.creation.box(extents=[0.05, 0.2, 0.05])
            leg.visual.face_colors = WOOD
            scene.add_geometry(leg, transform=trimesh.transformations.translation_matrix([x, 0.1, z]))

    bed_base = trimesh.creation.box(extents=[1.2, 0.2, 2])
    bed_base.visual.face_colors = WOOD
    scene.add_geometry(bed_base, transform=trimesh.transformations.translation_matrix([0, 0.3, 0]))

    headboard = trimesh.creation.box(extents=[1.2, 0.8, 0.05])
    headboard.visual.face_colors = WOOD
    scene.add_geometry(headboard, transform=trimesh.transformations.translation_matrix([0, 0.6, -1.0]))

    mattress = trimesh.creation.box(extents=[1.15, 0.2, 1.95])
    mattress.visual.face_colors = OFF_WHITE
    scene.add_geometry(mattress, transform=trimesh.transformations.translation_matrix([0, 0.5, 0]))

    # Pillows
    for x in [-0.3, 0.3]:
        pillow = trimesh.creation.box(extents=[0.4, 0.1, 0.3])
        pillow.visual.face_colors = WHITE
        scene.add_geometry(pillow, transform=trimesh.transformations.translation_matrix([x, 0.65, -0.8]))

    # Neatly folded towels
    towels = trimesh.creation.box(extents=[0.4, 0.1, 0.3])
    towels.visual.face_colors = WHITE
    scene.add_geometry(towels, transform=trimesh.transformations.translation_matrix([0, 0.65, 0.5]))

    # --- SIDE TABLE ---
    side_table = trimesh.creation.box(extents=[0.4, 0.45, 0.4])
    side_table.visual.face_colors = WOOD_LIGHT
    scene.add_geometry(side_table, transform=trimesh.transformations.translation_matrix([-0.9, 0.225, -0.5]))

    # Drawer line
    drawer_line = trimesh.creation.box(extents=[0.41, 0.01, 0.41])
    drawer_line.visual.face_colors = BLACK
    scene.add_geometry(drawer_line, transform=trimesh.transformations.translation_matrix([-0.9, 0.3, -0.5]))

    # Handle
    handle = trimesh.creation.box(extents=[0.1, 0.02, 0.02])
    handle.visual.face_colors = METAL
    scene.add_geometry(handle, transform=trimesh.transformations.translation_matrix([-0.7, 0.35, -0.5]))

    # WiFi Router
    router_body = trimesh.creation.box(extents=[0.15, 0.03, 0.1])
    router_body.visual.face_colors = BLACK
    scene.add_geometry(router_body, transform=trimesh.transformations.translation_matrix([-0.9, 0.465, -0.5]))

    # Antennas
    for x in [-0.05, 0.05]:
        ant = trimesh.creation.cylinder(radius=0.005, height=0.1)
        ant.visual.face_colors = BLACK
        scene.add_geometry(ant, transform=trimesh.transformations.translation_matrix([-0.9 + x, 0.515, -0.54]))

    # Glass Water Purifier
    purifier_base = trimesh.creation.cylinder(radius=0.08, height=0.2)
    purifier_base.visual.face_colors = PURIFIER_GLASS
    scene.add_geometry(purifier_base, transform=trimesh.transformations.translation_matrix([-0.9, 0.55, -0.65]))

    # --- STUDY DESK ---
    desk_top = trimesh.creation.box(extents=[1.2, 0.05, 0.6])
    desk_top.visual.face_colors = DARK_GREY
    scene.add_geometry(desk_top, transform=trimesh.transformations.translation_matrix([1.3, 0.75, -1.6]))

    # 4 Legs
    for x in [0.75, 1.85]:
        for z in [-1.35, -1.85]:
            leg = trimesh.creation.box(extents=[0.05, 0.75, 0.05])
            leg.visual.face_colors = METAL
            scene.add_geometry(leg, transform=trimesh.transformations.translation_matrix([x, 0.375, z]))

    # Drawers under desk
    drawer_block = trimesh.creation.box(extents=[0.3, 0.3, 0.5])
    drawer_block.visual.face_colors = WOOD_LIGHT
    scene.add_geometry(drawer_block, transform=trimesh.transformations.translation_matrix([1.7, 0.55, -1.6]))

    # UPS Unit (below desk)
    ups = trimesh.creation.box(extents=[0.2, 0.3, 0.4])
    ups.visual.face_colors = BLACK
    scene.add_geometry(ups, transform=trimesh.transformations.translation_matrix([0.9, 0.15, -1.7]))

    # --- ERGONOMIC CHAIR ---
    # Base/Wheels
    chair_stem = trimesh.creation.cylinder(radius=0.03, height=0.4)
    chair_stem.visual.face_colors = METAL
    scene.add_geometry(chair_stem, transform=trimesh.transformations.translation_matrix([1.3, 0.2, -1.0]))

    # "Wheels" area
    chair_base = trimesh.creation.box(extents=[0.4, 0.02, 0.4])
    chair_base.visual.face_colors = BLACK
    scene.add_geometry(chair_base, transform=trimesh.transformations.translation_matrix([1.3, 0.05, -1.0]))

    chair_seat = trimesh.creation.box(extents=[0.45, 0.08, 0.45])
    chair_seat.visual.face_colors = BLACK
    scene.add_geometry(chair_seat, transform=trimesh.transformations.translation_matrix([1.3, 0.45, -1.0]))

    chair_back = trimesh.creation.box(extents=[0.45, 0.6, 0.05])
    chair_back.visual.face_colors = BLACK
    scene.add_geometry(chair_back, transform=trimesh.transformations.translation_matrix([1.3, 0.75, -0.8]))

    # Armrests
    for x in [1.05, 1.55]:
        arm = trimesh.creation.box(extents=[0.05, 0.2, 0.3])
        arm.visual.face_colors = BLACK
        scene.add_geometry(arm, transform=trimesh.transformations.translation_matrix([x, 0.6, -1.0]))

    # --- SPLIT AC ---
    ac_body = trimesh.creation.box(extents=[1.0, 0.25, 0.2])
    ac_body.visual.face_colors = WHITE
    scene.add_geometry(ac_body, transform=trimesh.transformations.translation_matrix([0, 2.3, -1.85]))

    # Louver
    louver = trimesh.creation.box(extents=[0.9, 0.02, 0.15])
    louver.visual.face_colors = LIGHT_GREY
    scene.add_geometry(louver, transform=trimesh.transformations.translation_matrix([0, 2.2, -1.8]))

    # CCTV Camera (Dome)
    cctv_base = trimesh.creation.cylinder(radius=0.06, height=0.02)
    cctv_base.visual.face_colors = LIGHT_GREY
    scene.add_geometry(cctv_base, transform=trimesh.transformations.translation_matrix([-1.9, 2.65, -1.9]))

    cctv_dome = trimesh.creation.uv_sphere(radius=0.05)
    cctv_dome.visual.face_colors = BLACK
    scene.add_geometry(cctv_dome, transform=trimesh.transformations.translation_matrix([-1.9, 2.6, -1.9]))

    # --- WARDROBE ---
    wardrobe = trimesh.creation.box(extents=[1.0, 2.2, 0.6])
    wardrobe.visual.face_colors = WOOD
    scene.add_geometry(wardrobe, transform=trimesh.transformations.translation_matrix([-1.4, 1.1, 1.0]))

    # Door line
    door_line = trimesh.creation.box(extents=[0.01, 2.2, 0.61])
    door_line.visual.face_colors = BLACK
    scene.add_geometry(door_line, transform=trimesh.transformations.translation_matrix([-1.4, 1.1, 1.0]))

    # Handles
    for y in [1.1, 1.3]:
        h1 = trimesh.creation.box(extents=[0.02, 0.2, 0.02])
        h1.visual.face_colors = METAL
        scene.add_geometry(h1, transform=trimesh.transformations.translation_matrix([-1.08, 1.1, 1.1]))
        scene.add_geometry(h1, transform=trimesh.transformations.translation_matrix([-1.08, 1.1, 0.9]))

    # Bean Bag
    bean_bag = trimesh.creation.uv_sphere(radius=0.45, count=[32, 32])
    bean_bag.visual.face_colors = PINK
    scene.add_geometry(bean_bag, transform=trimesh.transformations.translation_matrix([1.4, 0.4, 1.4]))

    # Laundry Basket
    laundry = trimesh.creation.cylinder(radius=0.22, height=0.6)
    laundry.visual.face_colors = LIGHT_GREY
    scene.add_geometry(laundry, transform=trimesh.transformations.translation_matrix([-1.4, 0.3, 0.2]))

    # Vacuum Cleaner
    vac_body = trimesh.creation.box(extents=[0.3, 0.25, 0.5])
    vac_body.visual.face_colors = BLUE
    scene.add_geometry(vac_body, transform=trimesh.transformations.translation_matrix([-1.4, 0.125, 1.8]))

    vac_pipe = trimesh.creation.cylinder(radius=0.02, height=1.0)
    vac_pipe.visual.face_colors = METAL
    scene.add_geometry(vac_pipe, transform=trimesh.transformations.translation_matrix([-1.4, 0.6, 1.8]))

    # Export to GLB
    scene.export('room.glb')
    print("room.glb generated successfully.")

if __name__ == '__main__':
    create_room()
