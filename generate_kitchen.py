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
    BLACK = [0, 0, 0, 255]
    OIL_COLOR = [218, 165, 32, 200]

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

    # L-shaped Countertop
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

    # Overhead Cabinets
    cabinet_above = trimesh.creation.box(extents=[2.4, 0.7, 0.3])
    cabinet_above.visual.face_colors = WOOD
    scene.add_geometry(cabinet_above, transform=trimesh.transformations.translation_matrix([0.3, 1.85, -1.35]))

    # Chimney Hood
    chimney_base = trimesh.creation.box(extents=[0.6, 0.1, 0.4])
    chimney_base.visual.face_colors = STAINLESS
    scene.add_geometry(chimney_base, transform=trimesh.transformations.translation_matrix([0, 1.6, -1.3]))

    chimney_pipe = trimesh.creation.cylinder(radius=0.1, height=1.1)
    chimney_pipe.visual.face_colors = STAINLESS
    scene.add_geometry(chimney_pipe, transform=trimesh.transformations.translation_matrix([0, 2.15, -1.3]))

    # Two-burner Gas Stove
    stove = trimesh.creation.box(extents=[0.6, 0.05, 0.4])
    stove.visual.face_colors = STAINLESS
    scene.add_geometry(stove, transform=trimesh.transformations.translation_matrix([0, 0.95, -1.2]))

    burner1 = trimesh.creation.cylinder(radius=0.08, height=0.02)
    burner1.visual.face_colors = BLACK
    scene.add_geometry(burner1, transform=trimesh.transformations.translation_matrix([-0.15, 0.98, -1.2]))

    burner2 = trimesh.creation.cylinder(radius=0.08, height=0.02)
    burner2.visual.face_colors = BLACK
    scene.add_geometry(burner2, transform=trimesh.transformations.translation_matrix([0.15, 0.98, -1.2]))

    # Cooking essentials and oil bottles
    oil_bottle = trimesh.creation.cylinder(radius=0.03, height=0.15)
    oil_bottle.visual.face_colors = OIL_COLOR
    scene.add_geometry(oil_bottle, transform=trimesh.transformations.translation_matrix([-0.4, 1.0, -1.3]))

    spice_jar = trimesh.creation.cylinder(radius=0.02, height=0.08)
    spice_jar.visual.face_colors = WOOD
    scene.add_geometry(spice_jar, transform=trimesh.transformations.translation_matrix([-0.48, 0.965, -1.3]))

    # Sink
    sink = trimesh.creation.box(extents=[0.5, 0.1, 0.4])
    sink.visual.face_colors = STAINLESS
    scene.add_geometry(sink, transform=trimesh.transformations.translation_matrix([1.2, 0.85, 0.5]))

    faucet = trimesh.creation.cylinder(radius=0.02, height=0.3)
    faucet.visual.face_colors = STAINLESS
    scene.add_geometry(faucet, transform=trimesh.transformations.translation_matrix([1.2, 1.05, 0.7]))

    # Water Purifier (wall mounted)
    purifier = trimesh.creation.box(extents=[0.3, 0.5, 0.2])
    purifier.visual.face_colors = WHITE
    scene.add_geometry(purifier, transform=trimesh.transformations.translation_matrix([1.4, 1.8, -0.5]))

    # Gas Cylinder
    cylinder = trimesh.creation.cylinder(radius=0.15, height=0.45)
    cylinder.visual.face_colors = RED
    scene.add_geometry(cylinder, transform=trimesh.transformations.translation_matrix([0.6, 0.225, -1.2]))

    # Lower Cabinets
    lower_cabinets = trimesh.creation.box(extents=[2.4, 0.85, 0.58])
    lower_cabinets.visual.face_colors = WOOD
    scene.add_geometry(lower_cabinets, transform=trimesh.transformations.translation_matrix([0.3, 0.425, -1.21]))

    # Export to GLB
    scene.export('kitchen.glb')
    print("kitchen.glb generated successfully.")

if __name__ == '__main__':
    create_kitchen()
