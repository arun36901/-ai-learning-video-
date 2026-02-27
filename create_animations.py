from moviepy.editor import *
import os

def create_title_animation():
    bg = ColorClip((1920, 1080), color=(26, 26, 46), duration=2)
    title = TextClip('HOW DOES AI LEARN?', fontsize=100, color='white', font='Arial-Bold')
    title = title.set_pos('center').set_duration(2)
    title = title.crossfadein(1)
    subtitle = TextClip('The Truth About Machine Learning', fontsize=50, color='#e94560', font='Arial')
    subtitle = subtitle.set_pos(('center', 150)).set_duration(2)
    subtitle = subtitle.set_start(0.5).crossfadein(0.5)
    final = CompositeVideoClip([bg, title, subtitle])
    final.write_videofile('clips/clip1_title.mp4', fps=24, codec='libx264')
    print("✅ Created: clip1_title.mp4")

def create_chess_animation():
    bg = ColorClip((1920, 1080), color=(26, 26, 46), duration=3)
    piece = TextClip('♟', fontsize=200, color='#e94560', font='Arial')
    piece = piece.set_pos(('center', 'center')).set_duration(3)
    piece = piece.set_pos(lambda t: ('center', 'center' + 50*t - 100))
    text = TextClip('AI Learned Chess in 4 Hours', fontsize=60, color='white', font='Arial')
    text = text.set_pos(('center', 800)).set_duration(3)
    final = CompositeVideoClip([bg, piece, text])
    final.write_videofile('clips/clip2_chess.mp4', fps=24, codec='libx264')
    print("✅ Created: clip2_chess.mp4")

def create_pattern_animation():
    bg = ColorClip((1920, 1080), color=(26, 26, 46), duration=3)
    cats = []
    positions = [(400, 300), (760, 300), (1120, 300), (580, 500), (940, 500)]
    for i, pos in enumerate(positions):
        cat = TextClip('🐱', fontsize=80, font='Arial')
        cat = cat.set_pos(pos).set_duration(3)
        cat = cat.set_start(i * 0.3).crossfadein(0.3)
        cats.append(cat)
    text = TextClip('Finding Patterns...', fontsize=50, color='#e94560', font='Arial')
    text = text.set_pos(('center', 800)).set_duration(3)
    text = text.set_start(1).crossfadein(0.5)
    final = CompositeVideoClip([bg, *cats, text])
    final.write_videofile('clips/clip3_pattern.mp4', fps=24, codec='libx264')
    print("✅ Created: clip3_pattern.mp4")

def create_neural_animation():
    bg = ColorClip((1920, 1080), color=(26, 26, 46), duration=4)
    nodes = []
    positions = [(960, 200), (700, 400), (960, 400), (1220, 400),
                 (500, 600), (800, 600), (1120, 600), (1400, 600)]
    for i, pos in enumerate(positions):
        node = TextClip('●', fontsize=40, color='#e94560', font='Arial')
        node = node.set_pos(pos).set_duration(4)
        node = node.set_start(i * 0.2).crossfadein(0.2)
        nodes.append(node)
    text = TextClip('Neural Networks: Million of Connections', fontsize=50, color='white', font='Arial')
    text = text.set_pos(('center', 800)).set_duration(4)
    final = CompositeVideoClip([bg, *nodes, text])
    final.write_videofile('clips/clip4_neural.mp4', fps=24, codec='libx264')
    print("✅ Created: clip4_neural.mp4")

def create_subscribe_animation():
    bg = ColorClip((1920, 1080), color=(26, 26, 46), duration=2)
    button = ColorClip((400, 100), color='#e94560', duration=2)
    button = button.set_pos(('center', 500))
    button = button.crossfadein(0.5)
    button_text = TextClip('SUBSCRIBE', fontsize=50, color='white', font='Arial-Bold')
    button_text = button_text.set_pos(('center', 520)).set_duration(2)
    button_text = button_text.set_start(0.3).crossfadein(0.3)
    title = TextClip('If This Blew Your Mind...', fontsize=60, color='white', font='Arial')
    title = title.set_pos(('center', 350)).set_duration(2)
    title = title.crossfadein(0.5)
    final = CompositeVideoClip([bg, title, button, button_text])
    final.write_videofile('clips/clip5_subscribe.mp4', fps=24, codec='libx264')
    print("✅ Created: clip5_subscribe.mp4")

def main():
    if not os.path.exists('clips'):
        os.makedirs('clips')
    print("🎬 Creating animated clips...\n")
    create_title_animation()
    create_chess_animation()
    create_pattern_animation()
    create_neural_animation()
    create_subscribe_animation()
    print("\n🎉 All clips created!")

if __name__ == '__main__':
    main()
