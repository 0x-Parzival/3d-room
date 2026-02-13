import trimesh
import numpy as np

def create_kitchen():
    scene = trimesh.Scene()

    # Colors (RGBA)
    WOOD = [101, 67, 33, 255] # Dark wood
    GRANITE = [30, 30, 30, 255] # Black granite
    STAINLESS = [192, 192, 192, 255] # Stainless steel
    MOSAIC = [150, 150, 150, 255] # Grey-ish mosaic
    WHITE = [255, 255, 255, 255]
    RED = [200, 0, 0, 255] # Gas cylinder
    BLACK = [20, 20, 20, 255]
    OIL_COLOR = [218, 165, 32, 200]
    METAL = [210, 210, 210, 255]

    # Floor
    floor = trimesh.creation.box(extents=[3, 0.1, 3])
    floor.visual.face_colors = [230, 230, 230, 255]
    scene.add_geometry(floor, transform=trimesh.transformations.translation_matrix([0, -0.05, 0]))

    # Walls
    wall_back = trimesh.creation.box(extents=[3, 2.7, 0.1])
    wall_back.visual.face_colors = WHITE
    scene.add_geometry(wall_back, transform=trimesh.transformations.translation_matrix([0, 1.35, -1.5]))

    wall_right = trimesh.creation.box(extents=[0.1, 2.7, 3])
    wall_right.visual.face_colors = WHITE
    scene.add_geometry(wall_right, transform=trimesh.transformations.translation_matrix([1.5, 1.35, 0]))

    # --- COUNTERTOP ---
    counter1 = trimesh.creation.box(extents=[2.4, 0.05, 0.6])
    counter1.visual.face_colors = GRANITE
    scene.add_geometry(counter1, transform=trimesh.transformations.translation_matrix([0.3, 0.9, -1.2]))

    counter2 = trimesh.creation.box(extents=[0.6, 0.05, 1.8])
    counter2.visual.face_colors = GRANITE
    scene.add_geometry(counter2, transform=trimesh.transformations.translation_matrix([1.2, 0.9, 0]))

    # Mosaic Backsplash
    backsplash1 = trimesh.creation.box(extents=[2.4, 0.6, 0.02])
    backsplash1.visual.face_colors = MOSAIC
    scene.add_geometry(backsplash1, transform=trimesh.transformations.translation_matrix([0.3, 1.2, -1.48]))

    # --- OVERHEAD CABINETS ---
    overhead = trimesh.creation.box(extents=[2.4, 0.7, 0.3])
    overhead.visual.face_colors = WOOD
    scene.add_geometry(overhead, transform=trimesh.transformations.translation_matrix([0.3, 1.85, -1.35]))

    # Door lines & handles
    for x in [-0.7, -0.1, 0.5, 1.1]:
        line = trimesh.creation.box(extents=[0.01, 0.7, 0.31])
        line.visual.face_colors = BLACK
        scene.add_geometry(line, transform=trimesh.transformations.translation_matrix([x, 1.85, -1.35]))

        handle = trimesh.creation.box(extents=[0.02, 0.1, 0.02])
        handle.visual.face_colors = STAINLESS
        scene.add_geometry(handle, transform=trimesh.transformations.translation_matrix([x + 0.1, 1.6, -1.18]))

    # --- CHIMNEY HOOD ---
    chimney_base = trimesh.creation.box(extents=[0.6, 0.1, 0.4])
    chimney_base.visual.face_colors = STAINLESS
    scene.add_geometry(chimney_base, transform=trimesh.transformations.translation_matrix([0, 1.6, -1.3]))

    chimney_slope = trimesh.creation.box(extents=[0.5, 0.3, 0.3])
    chimney_slope.visual.face_colors = STAINLESS
    scene.add_geometry(chimney_slope, transform=trimesh.transformations.translation_matrix([0, 1.8, -1.3]))

    chimney_pipe = trimesh.creation.cylinder(radius=0.08, height=0.8)
    chimney_pipe.visual.face_colors = STAINLESS
    scene.add_geometry(chimney_pipe, transform=trimesh.transformations.translation_matrix([0, 2.3, -1.3]))

    # --- STOVE ---
    stove = trimesh.creation.box(extents=[0.6, 0.06, 0.4])
    stove.visual.face_colors = STAINLESS
    scene.add_geometry(stove, transform=trimesh.transformations.translation_matrix([0, 0.95, -1.2]))

    for x in [-0.15, 0.15]:
        # Burner base
        burner_b = trimesh.creation.cylinder(radius=0.08, height=0.02)
        burner_b.visual.face_colors = BLACK
        scene.add_geometry(burner_b, transform=trimesh.transformations.translation_matrix([x, 0.98, -1.2]))
        # Burner top (ring)
        burner_t = trimesh.creation.cylinder(radius=0.06, height=0.03)
        burner_t.visual.face_colors = [40, 40, 40, 255]
        scene.add_geometry(burner_t, transform=trimesh.transformations.translation_matrix([x, 1.0, -1.2]))

        # Knob
        knob = trimesh.creation.cylinder(radius=0.02, height=0.03)
        knob.visual.face_colors = BLACK
        scene.add_geometry(knob, transform=trimesh.transformations.translation_matrix([x, 0.95, -1.0]))

    # Cooking essentials
    oil_bottle = trimesh.creation.cylinder(radius=0.03, height=0.15)
    oil_bottle.visual.face_colors = OIL_COLOR
    scene.add_geometry(oil_bottle, transform=trimesh.transformations.translation_matrix([-0.4, 1.0, -1.3]))
    cap = trimesh.creation.cylinder(radius=0.015, height=0.02)
    cap.visual.face_colors = WHITE
    scene.add_geometry(cap, transform=trimesh.transformations.translation_matrix([-0.4, 1.08, -1.3]))

    # --- SINK & FAUCET ---
    sink = trimesh.creation.box(extents=[0.5, 0.1, 0.4])
    sink.visual.face_colors = STAINLESS
    scene.add_geometry(sink, transform=trimesh.transformations.translation_matrix([1.2, 0.85, 0.5]))

    # Detailed Faucet
    f_base = trimesh.creation.cylinder(radius=0.02, height=0.1)
    f_base.visual.face_colors = STAINLESS
    scene.add_geometry(f_base, transform=trimesh.transformations.translation_matrix([1.2, 0.95, 0.75]))

    f_neck = trimesh.creation.box(extents=[0.02, 0.2, 0.15])
    f_neck.visual.face_colors = STAINLESS
    scene.add_geometry(f_neck, transform=trimesh.transformations.translation_matrix([1.2, 1.1, 0.68]))

    # Water Purifier
    purifier = trimesh.creation.box(extents=[0.3, 0.5, 0.2])
    purifier.visual.face_colors = WHITE
    scene.add_geometry(purifier, transform=trimesh.transformations.translation_matrix([1.4, 1.8, -0.5]))
    p_dispenser = trimesh.creation.cylinder(radius=0.01, height=0.05)
    p_dispenser.visual.face_colors = STAINLESS
    scene.add_geometry(p_dispenser, transform=trimesh.transformations.translation_matrix([1.3, 1.6, -0.5]))

    # Gas Cylinder
    cylinder = trimesh.creation.cylinder(radius=0.15, height=0.45)
    cylinder.visual.face_colors = RED
    scene.add_geometry(cylinder, transform=trimesh.transformations.translation_matrix([0.6, 0.225, -1.2]))
    c_cap = trimesh.creation.cylinder(radius=0.05, height=0.05)
    c_cap.visual.face_colors = RED
    scene.add_geometry(c_cap, transform=trimesh.transformations.translation_matrix([0.6, 0.45, -1.2]))

    # Lower Cabinets
    lower_cabinets = trimesh.creation.box(extents=[2.4, 0.85, 0.58])
    lower_cabinets.visual.face_colors = WOOD
    scene.add_geometry(lower_cabinets, transform=trimesh.transformations.translation_matrix([0.3, 0.425, -1.21]))

    # Door lines for lower cabinets
    for x in [-0.7, 0.1, 0.9]:
        line = trimesh.creation.box(extents=[0.01, 0.85, 0.6])
        line.visual.face_colors = BLACK
        scene.add_geometry(line, transform=trimesh.transformations.translation_matrix([x, 0.425, -1.21]))

    # Export to GLB
    scene.export('kitchen.glb')
    print("kitchen.glb generated successfully.")

if __name__ == '__main__':
    create_kitchen()
