import React, { Suspense, useEffect, useRef, useState } from 'react';
import { Canvas, useFrame, useThree } from '@react-three/fiber';
import { OrbitControls, useGLTF, Html, PerspectiveCamera, Environment, ContactShadows } from '@react-three/drei';
import * as THREE from 'three';

const roomLabels = [
    { key: 'bed_base', title: 'Premium Furnished', text: 'Comfortable single bed with fresh linen.', pos: [-1.0, 0.5, 0.5] },
    { key: 'wifi_router', title: 'High-Speed WiFi', text: 'Seamless connectivity for work & study.', pos: [1.7, 1.0, -1.2] },
    { key: 'cctv_camera', title: '24/7 Security', text: 'Ensuring a safe living environment.', pos: [1.8, 2.4, -1.8] },
    { key: 'meal_plate', title: 'Meals Included', text: '4 Nutritious meals provided daily.', pos: [0.8, 1.0, -1.0] },
    { key: 'ups_unit', title: 'Power Backup', text: 'Uninterrupted power supply.', pos: [1.7, 0.4, -1.2] },
    { key: 'cleaning_broom', title: 'Daily Cleaning', text: 'Hassle-free maintenance.', pos: [-1.8, 1.2, -1.8] }
];

function Model() {
    const { scene } = useGLTF('/models/room.glb');
    const humanRef = useRef<THREE.Group>(null!);
    const torsoRef = useRef<THREE.Object3D>(null!);
    const armRU = useRef<THREE.Object3D>(null!);
    const armRL = useRef<THREE.Object3D>(null!);
    const legLU = useRef<THREE.Object3D>(null!);
    const legRU = useRef<THREE.Object3D>(null!);

    useEffect(() => {
        scene.traverse((node) => {
            if (node.name === 'human_root') humanRef.current = node as THREE.Group;
            if (node.name === 'human_torso') torsoRef.current = node;
            if (node.name === 'human_arm_r_u') armRU.current = node;
            if (node.name === 'human_arm_r_l') armRL.current = node;
            if (node.name === 'human_leg_l_u') legLU.current = node;
            if (node.name === 'human_leg_r_u') legRU.current = node;

            if ((node as THREE.Mesh).isMesh) {
                node.castShadow = true;
                node.receiveShadow = true;
                const mesh = node as THREE.Mesh;
                const mat = mesh.material as THREE.MeshStandardMaterial;
                if (node.name.includes('wood')) {
                    mat.roughness = 0.7;
                    mat.metalness = 0.1;
                }
                if (node.name.includes('metal')) {
                    mat.metalness = 0.9;
                    mat.roughness = 0.1;
                }
                if (node.name.includes('glass')) {
                    mat.transparent = true;
                    mat.opacity = 0.3;
                    mat.metalness = 0.5;
                    mat.roughness = 0.1;
                }
                if (node.name.includes('linen') || node.name.includes('pillow')) {
                    mat.roughness = 1.0;
                    mat.metalness = 0.0;
                }
                if (node.name.includes('desk')) {
                    // Make it look like granite as per request
                    mat.color.set('#222');
                    mat.roughness = 0.1;
                    mat.metalness = 0.2;
                }
                if (node.name.includes('wall')) {
                    mat.roughness = 0.9;
                }
            }
        });
    }, [scene]);

    useFrame((state) => {
        const time = state.clock.getElapsedTime() % 10;

        if (humanRef.current && torsoRef.current) {
            const deskPos = new THREE.Vector3(1.1, 0.05, -0.8);
            const bedPos = new THREE.Vector3(-1.0, 0.4, 0.5);

            if (time < 7) {
                // Desk Actions
                humanRef.current.position.copy(deskPos);
                humanRef.current.rotation.set(0, 0, 0);

                if (time < 3) {
                    armRU.current.rotation.x = -Math.PI / 4;
                    armRL.current.rotation.x = -Math.PI / 4;
                } else if (time < 5) {
                    const t = (time - 3) / 2;
                    const drinkAngle = Math.sin(t * Math.PI) * 1.5;
                    armRU.current.rotation.x = -Math.PI / 4 - drinkAngle;
                } else {
                    const t = (time - 5) / 2;
                    const reachAngle = Math.sin(t * Math.PI) * 1.2;
                    armRU.current.rotation.x = -Math.PI / 4 - reachAngle;
                }
            } else if (time < 9.5) {
                // Transition to Bed and Sleep
                const t = (time - 7) / 0.5;
                if (t < 1) {
                    humanRef.current.position.lerpVectors(deskPos, bedPos, t);
                    humanRef.current.rotation.z = (Math.PI / 2) * t;
                } else {
                    humanRef.current.position.copy(bedPos);
                    humanRef.current.rotation.z = Math.PI / 2;
                    humanRef.current.rotation.y = Math.PI / 2;
                }
            } else {
                // Transition back to Desk
                const t = (time - 9.5) / 0.5;
                humanRef.current.position.lerpVectors(bedPos, deskPos, t);
                humanRef.current.rotation.z = (Math.PI / 2) * (1 - t);
            }
            torsoRef.current.scale.y = 1 + Math.sin(time * 2) * 0.01;
        }
    });

    return <primitive object={scene} />;
}

function Label({ label, index, visibleCount }: { label: any, index: number, visibleCount: number }) {
    if (index >= visibleCount) return null;

    return (
        <Html distanceFactor={8} position={label.pos}>
            <div className="animate-fade-in pointer-events-none select-none" style={{ width: '150px' }}>
                <div className="bg-white/90 backdrop-blur-sm p-2 rounded-lg border-l-4 border-[#2e8b57] shadow-xl">
                    <div className="text-[#2e8b57] font-bold text-xs">{label.title}</div>
                    <div className="text-gray-600" style={{ fontSize: '10px', lineHeight: '1.2' }}>{label.text}</div>
                </div>
                <div className="w-2 h-2 bg-[#2e8b57] rounded-full mx-auto -mt-1 border border-white" />
            </div>
        </Html>
    );
}

function CameraController() {
    const { camera } = useThree();
    useFrame((state) => {
        const time = state.clock.getElapsedTime();
        // Slow premium drift
        camera.position.x = 5 + Math.sin(time * 0.15) * 0.3;
        camera.position.y = 4 + Math.cos(time * 0.1) * 0.2;
        camera.position.z = 5 + Math.cos(time * 0.15) * 0.3;
        camera.lookAt(0, 0.5, 0);
    });
    return null;
}

const ThreeDRoom: React.FC = () => {
    const [visibleCount, setVisibleCount] = useState(0);

    useEffect(() => {
        const interval = setInterval(() => {
            setVisibleCount(prev => (prev < roomLabels.length ? prev + 1 : prev));
        }, 1500);
        return () => clearInterval(interval);
    }, []);

    return (
        <div className="w-full h-screen bg-gradient-to-br from-gray-100 to-gray-300">
            <Canvas shadows className="outline-none">
                <PerspectiveCamera makeDefault fov={25} position={[5, 5, 5]} />
                <CameraController />
                <OrbitControls enableDamping dampingFactor={0.05} />

                <ambientLight intensity={0.6} color="#ffd1a1" />
                <directionalLight
                    position={[5, 10, 5]}
                    intensity={1.5}
                    castShadow
                    shadow-mapSize={[2048, 2048]}
                />
                <pointLight position={[-5, 5, -5]} intensity={0.5} color="#cacaff" />

                <Suspense fallback={null}>
                    <Model />
                    {roomLabels.map((l, i) => (
                        <Label key={l.key} label={l} index={i} visibleCount={visibleCount} />
                    ))}
                    <Environment preset="city" />
                    <ContactShadows opacity={0.4} scale={10} blur={2} far={10} resolution={256} color="#000000" />
                </Suspense>
            </Canvas>

            <style>{`
                @keyframes fadeIn {
                    from { opacity: 0; transform: translateY(10px); }
                    to { opacity: 1; transform: translateY(0); }
                }
                .animate-fade-in {
                    animation: fadeIn 0.8s ease-out forwards;
                }
                .bg-white\\/90 { background-color: rgba(255, 255, 255, 0.9); }
                .backdrop-blur-sm { backdrop-filter: blur(4px); }
                .p-2 { padding: 0.3rem; }
                .rounded-lg { border-radius: 0.4rem; }
                .border-l-4 { border-left-width: 3px; }
                .border-\\[\\#2e8b57\\] { border-color: #2e8b57; }
                .shadow-xl { box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); }
                .text-\\[\\#2e8b57\\] { color: #2e8b57; }
                .font-bold { font-weight: 700; }
                .text-xs { font-size: 0.65rem; }
                .text-gray-600 { color: #4b5563; font-size: 0.55rem; }
                .rounded-full { border-radius: 9999px; }
                .mx-auto { margin-left: auto; margin-right: auto; }
                .-mt-1 { margin-top: -0.25rem; }
            `}</style>

            <div className="absolute top-10 left-10 pointer-events-none">
                <h1 className="text-4xl font-extrabold text-[#2e8b57] drop-shadow-md">Mother Homes</h1>
                <p className="text-gray-700 font-medium">Safe • Furnished • Hassle-Free Living</p>
            </div>
        </div>
    );
};

export default ThreeDRoom;
