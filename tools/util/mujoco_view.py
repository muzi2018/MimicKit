import mujoco
print(mujoco.__version__)

# Load model
m = mujoco.MjModel.from_xml_path('/home/wang/GMR/assets/unitree_g1/g1_mocap_29dof.xml')

print("=== BODY LIST ===")
for i in range(m.nbody):
    print(f"{i:02d}: {m.body(i).name}")

print("\n=== JOINT LIST ===")
for i in range(m.njnt):
    j = m.joint(i)
    jtype = mujoco.mjtJoint(j.type).name   # convert enum to readable string
    print(f"{i:02d}: {j.name} | type={jtype} | qpos_adr={m.jnt_qposadr[i]} | qvel_adr={m.jnt_dofadr[i]}")
