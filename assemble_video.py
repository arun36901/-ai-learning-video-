from moviepy.editor import *
import os

def create_final_video():
    print("🎞️ Assembling final video...")
    
    if not os.path.exists('clips'):
        os.makedirs('clips')
    
    clips = []
    clip1 = VideoFileClip('clips/clip1_title.mp4')
    clips.append(clip1)
    clip2 = VideoFileClip('clips/clip2_chess.mp4')
    clips.append(clip2)
    clip3 = VideoFileClip('clips/clip3_pattern.mp4')
    clips.append(clip3)
    clip4 = VideoFileClip('clips/clip4_neural.mp4')
    clips.append(clip4)
    clip5 = VideoFileClip('clips/clip5_subscribe.mp4')
    clips.append(clip5)
    
    final_clip = concatenate_videoclips(clips, method='compose')
    final_clip.write_videofile('final_video.mp4', fps=24, codec='libx264')
    print("\n🎉 DONE! Your video is ready: final_video.mp4")

if __name__ == '__main__':
    create_final_video()
