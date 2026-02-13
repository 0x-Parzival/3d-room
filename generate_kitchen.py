import trimesh
import numpy as np

def create_human(scene, pos, rot_y=0, state='standing', name_prefix='human'):
    # Colors
    SKIN = [255, 220, 180, 255]
    SHIRT = [200, 50, 50, 255]
    PANTS = [50, 50, 50, 255]
    HAIR = [30, 20, 10, 255]

    # Torso
    torso = trimesh.creation.cylinder(radius=0.15, height=0.45)
    torso.visual.face_colors = SHIRT
    t_pos = [pos[0], pos[1] + 0.9, pos[2]]
    scene.add_geometry(torso, transform=trimesh.transformations.translation_matrix(t_pos), node_name=f'{name_prefix}_torso')

    # Head
    head = trimesh.creation.uv_sphere(radius=0.11)
    head.visual.face_colors = SKIN
    h_pos = [t_pos[0], t_pos[1] + 0.35, t_pos[2]]
    scene.add_geometry(head, transform=trimesh.transformations.translation_matrix(h_pos), node_name=f'{name_prefix}_head')

    # Legs
    for x_off in [-0.1, 0.1]:
        leg = trimesh.creation.cylinder(radius=0.07, height=0.8)
        leg.visual.face_colors = PANTS
        l_trans = trimesh.transformations.translation_matrix([pos[0] + x_off, pos[1] + 0.4, pos[2]])
        scene.add_geometry(leg, transform=l_trans)

def create_kitchen():
    scene = trimesh.Scene()

    # Colors
    WOOD = [101, 67, 33, 255]
    GRANITE = [30, 30, 30, 255]
    STAINLESS = [192, 192, 192, 255]
    MOSAIC = [160, 160, 160, 255]
    WHITE = [250, 250, 250, 255]
    RED = [180, 0, 0, 255]

    # Floor & Walls
    scene.add_geometry(trimesh.creation.box(extents=[3, 0.1, 3]), transform=trimesh.transformations.translation_matrix([0, -0.05, 0]))
    scene.add_geometry(trimesh.creation.box(extents=[3, 2.7, 0.1]), transform=trimesh.transformations.translation_matrix([0, 1.35, -1.5]))
    scene.add_geometry(trimesh.creation.box(extents=[0.1, 2.7, 3]), transform=trimesh.transformations.translation_matrix([1.5, 1.35, 0]))

    # --- COUNTERTOP ---
    counter = trimesh.creation.box(extents=[2.4, 0.05, 0.6])
    counter.visual.face_colors = GRANITE
    scene.add_geometry(counter, transform=trimesh.transformations.translation_matrix([0.3, 0.9, -1.2]))

    # Backsplash
    backsplash = trimesh.creation.box(extents=[2.4, 0.6, 0.02])
    backsplash.visual.face_colors = MOSAIC
    scene.add_geometry(backsplash, transform=trimesh.transformations.translation_matrix([0.3, 1.2, -1.48]))

    # --- CABINETS & CHIMNEY ---
    overhead = trimesh.creation.box(extents=[2.4, 0.7, 0.3])
    overhead.visual.face_colors = WOOD
    scene.add_geometry(overhead, transform=trimesh.transformations.translation_matrix([0.3, 1.85, -1.35]))

    chimney = trimesh.creation.box(extents=[0.6, 0.4, 0.4])
    chimney.visual.face_colors = STAINLESS
    scene.add_geometry(chimney, transform=trimesh.transformations.translation_matrix([0, 1.6, -1.3]))

    # --- STOVE & ESSENTIALS ---
    stove = trimesh.creation.box(extents=[0.6, 0.05, 0.4])
    stove.visual.face_colors = STAINLESS
    scene.add_geometry(stove, transform=trimesh.transformations.translation_matrix([0, 0.95, -1.2]))

    # Oil Bottles
    for i in range(2):
        bottle = trimesh.creation.cylinder(radius=0.03, height=0.15)
        bottle.visual.face_colors = [218, 165, 32, 200]
        scene.add_geometry(bottle, transform=trimesh.transformations.translation_matrix([-0.5, 1.0, -1.3 + i*0.1]))

    # --- SINK & PURIFIER ---
    sink = trimesh.creation.box(extents=[0.5, 0.1, 0.4])
    sink.visual.face_colors = STAINLESS
    scene.add_geometry(sink, transform=trimesh.transformations.translation_matrix([1.0, 0.85, -1.2]))

    faucet = trimesh.creation.cylinder(radius=0.02, height=0.2)
    faucet.visual.face_colors = STAINLESS
    scene.add_geometry(faucet, transform=trimesh.transformations.translation_matrix([1.0, 1.0, -1.4]))

    purifier = trimesh.creation.box(extents=[0.3, 0.5, 0.2])
    purifier.visual.face_colors = WHITE
    scene.add_geometry(purifier, transform=trimesh.transformations.translation_matrix([1.2, 1.6, -1.4]))

    # Gas Cylinder
    cylinder = trimesh.creation.cylinder(radius=0.15, height=0.45)
    cylinder.visual.face_colors = RED
    scene.add_geometry(cylinder, transform=trimesh.transformations.translation_matrix([0.6, 0.225, -1.2]))

    # Human
    create_human(scene, [0.4, 0, -0.8], state='standing', name_prefix='kitchen_human')

    # Lower Cabinets
    lower = trimesh.creation.box(extents=[2.4, 0.85, 0.58])
    lower.visual.face_colors = WOOD
    scene.add_geometry(lower, transform=trimesh.transformations.translation_matrix([0.3, 0.425, -1.21]))

    scene.export('kitchen.glb')
    print("kitchen.glb generated successfully.")

if __name__ == '__main__':
    create_kitchen()
