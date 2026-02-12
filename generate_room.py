import trimesh
import numpy as np

def create_room():
    scene = trimesh.Scene()

    # Colors (RGBA)
    WOOD = [139, 69, 19, 255]
    WHITE = [255, 255, 255, 255]
    DARK_GREY = [50, 50, 50, 255]
    LIGHT_GREY = [220, 220, 220, 255]
    BLUE = [100, 149, 237, 255]
    PINK = [255, 105, 180, 255]
    BLACK = [0, 0, 0, 255]
    METAL = [192, 192, 192, 255]
    PURIFIER_GLASS = [173, 216, 230, 180]

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

    # Bed
    bed_frame = trimesh.creation.box(extents=[1.2, 0.4, 2])
    bed_frame.visual.face_colors = WOOD
    scene.add_geometry(bed_frame, transform=trimesh.transformations.translation_matrix([0, 0.2, 0]))

    mattress = trimesh.creation.box(extents=[1.2, 0.15, 2])
    mattress.visual.face_colors = WHITE
    scene.add_geometry(mattress, transform=trimesh.transformations.translation_matrix([0, 0.475, 0]))

    # Neatly folded towels (small box on bed)
    towels = trimesh.creation.box(extents=[0.4, 0.05, 0.3])
    towels.visual.face_colors = [240, 240, 240, 255]
    scene.add_geometry(towels, transform=trimesh.transformations.translation_matrix([0, 0.575, 0.5]))

    # Side Table
    side_table = trimesh.creation.box(extents=[0.4, 0.4, 0.4])
    side_table.visual.face_colors = WOOD
    scene.add_geometry(side_table, transform=trimesh.transformations.translation_matrix([-0.9, 0.2, -0.5]))

    # WiFi Router
    router = trimesh.creation.box(extents=[0.15, 0.03, 0.1])
    router.visual.face_colors = BLACK
    scene.add_geometry(router, transform=trimesh.transformations.translation_matrix([-0.9, 0.415, -0.5]))

    # Glass Water Purifier (on side table)
    purifier_base = trimesh.creation.cylinder(radius=0.08, height=0.15)
    purifier_base.visual.face_colors = PURIFIER_GLASS
    scene.add_geometry(purifier_base, transform=trimesh.transformations.translation_matrix([-0.9, 0.475, -0.65]))

    # Study Desk
    desk_top = trimesh.creation.box(extents=[1.2, 0.05, 0.6])
    desk_top.visual.face_colors = DARK_GREY
    scene.add_geometry(desk_top, transform=trimesh.transformations.translation_matrix([1.3, 0.75, -1.6]))

    desk_leg1 = trimesh.creation.box(extents=[0.05, 0.75, 0.05])
    desk_leg1.visual.face_colors = METAL
    scene.add_geometry(desk_leg1, transform=trimesh.transformations.translation_matrix([0.75, 0.375, -1.35]))

    desk_leg2 = trimesh.creation.box(extents=[0.05, 0.75, 0.05])
    desk_leg2.visual.face_colors = METAL
    scene.add_geometry(desk_leg2, transform=trimesh.transformations.translation_matrix([1.85, 0.375, -1.35]))

    # UPS Unit (below desk)
    ups = trimesh.creation.box(extents=[0.2, 0.3, 0.4])
    ups.visual.face_colors = BLACK
    scene.add_geometry(ups, transform=trimesh.transformations.translation_matrix([1.3, 0.15, -1.7]))

    # Ergonomic Chair
    chair_seat = trimesh.creation.box(extents=[0.4, 0.05, 0.4])
    chair_seat.visual.face_colors = BLACK
    scene.add_geometry(chair_seat, transform=trimesh.transformations.translation_matrix([1.3, 0.45, -1.0]))

    chair_back = trimesh.creation.box(extents=[0.4, 0.5, 0.05])
    chair_back.visual.face_colors = BLACK
    scene.add_geometry(chair_back, transform=trimesh.transformations.translation_matrix([1.3, 0.7, -0.8]))

    # Split AC
    ac = trimesh.creation.box(extents=[1.0, 0.25, 0.2])
    ac.visual.face_colors = WHITE
    scene.add_geometry(ac, transform=trimesh.transformations.translation_matrix([0, 2.3, -1.85]))

    # CCTV Camera (Dome)
    cctv = trimesh.creation.uv_sphere(radius=0.05)
    cctv.visual.face_colors = BLACK
    scene.add_geometry(cctv, transform=trimesh.transformations.translation_matrix([-1.9, 2.6, -1.9]))

    # Wardrobe
    wardrobe = trimesh.creation.box(extents=[1.0, 2.0, 0.6])
    wardrobe.visual.face_colors = WOOD
    scene.add_geometry(wardrobe, transform=trimesh.transformations.translation_matrix([-1.4, 1.0, 1.0]))

    # Bean Bag
    bean_bag = trimesh.creation.uv_sphere(radius=0.4)
    bean_bag.visual.face_colors = PINK
    scene.add_geometry(bean_bag, transform=trimesh.transformations.translation_matrix([1.4, 0.4, 1.4]))

    # Laundry Basket
    laundry = trimesh.creation.cylinder(radius=0.2, height=0.5)
    laundry.visual.face_colors = LIGHT_GREY
    scene.add_geometry(laundry, transform=trimesh.transformations.translation_matrix([-1.4, 0.25, 0.2]))

    # Vacuum Cleaner
    vacuum = trimesh.creation.box(extents=[0.3, 0.2, 0.5])
    vacuum.visual.face_colors = BLUE
    scene.add_geometry(vacuum, transform=trimesh.transformations.translation_matrix([-1.4, 0.1, 1.8]))

    # Export to GLB
    scene.export('room.glb')
    print("room.glb generated successfully.")

if __name__ == '__main__':
    create_room()
