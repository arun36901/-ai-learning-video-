import subprocess
import sys

def run_script(script_name):
    print(f"\n🚀 Running {script_name}...")
    result = subprocess.run([sys.executable, script_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ {script_name} completed successfully!")
    else:
        print(f"❌ {script_name} failed!")
        print(result.stderr)
    return result.returncode

def main():
    print("=" * 50)
    print("🎬 AI LEARNING VIDEO GENERATOR")
    print("=" * 50)
    
    # Step 1: Generate graphics
    if run_script('generate_graphics.py') != 0:
        return
    
    # Step 2: Create animations
    if run_script('create_animations.py') != 0:
        return
    
    # Step 3: Assemble final video
    if run_script('assemble_video.py') != 0:
        return
    
    print("\n" + "=" * 50)
    print("🎉 ALL DONE! Your video is ready!")
    print("📁 Check: final_video.mp4")
    print("=" * 50)

if __name__ == '__main__':
    main()
