from PIL import Image, ImageDraw, ImageFont
import os

def create_folder():
    if not os.path.exists('assets'):
        os.makedirs('assets')
    print("✅ Folder 'assets' created!")

def create_background():
    width, height = 1920, 1080
    background = Image.new('RGB', (width, height), color='#1a1a2e')
    draw = ImageDraw.Draw(background)
    for y in range(height):
        draw.line([(0, y), (width, y)], fill=(26, 26, 46 + int(y/20)))
    background.save('assets/background.png')
    print("✅ Created: background.png")

def create_slide(filename, text, subtext=None, icon_type=None):
    width, height = 1920, 1080
    img = Image.new('RGB', (width, height), color='#1a1a2e')
    draw = ImageDraw.Draw(img)
    draw.ellipse([1400, 200, 1800, 600], fill='#16213e', outline='#0f3460', width=5)
    draw.ellipse([100, 700, 400, 1000], fill='#16213e', outline='#0f3460', width=5)
    
    if icon_type == 'chess':
        draw.rectangle([900, 300, 1020, 350], fill='#e94560')
        draw.ellipse([870, 280, 1050, 320], fill='#e94560')
        draw.rectangle([920, 350, 1000, 700], fill='#e94560')
        draw.ellipse([890, 680, 1030, 750], fill='#e94560')
    elif icon_type == 'computer':
        draw.rectangle([800, 300, 1120, 600], fill='#0f3460', outline='#e94560', width=3)
        draw.rectangle([820, 320, 1100, 580], fill='#16213e')
        draw.rectangle([900, 610, 1020, 750], fill='#0f3460')
        draw.rectangle([780, 750, 1140, 780], fill='#0f3460')
    elif icon_type == 'network':
        centers = [(960, 300), (800, 450), (960, 450), (1120, 450), 
                   (700, 600), (850, 600), (1070, 600), (1220, 600)]
        for cx, cy in centers:
            draw.ellipse([cx-30, cy-30, cx+30, cy+30], fill='#e94560', outline='#fff', width=2)
        draw.line([(960, 300), (800, 450)], fill='#0f3460', width=3)
        draw.line([(960, 300), (960, 450)], fill='#0f3460', width=3)
        draw.line([(960, 300), (1120, 450)], fill='#0f3460', width=3)
    elif icon_type == 'brain':
        draw.ellipse([800, 250, 1120, 650], fill='#e94560', outline='#fff', width=2)
        draw.ellipse([850, 300, 1070, 600], fill='#16213e')
        draw.arc([870, 320, 1050, 580], 0, 180, fill='#e94560', width=3)
        draw.arc([900, 340, 1020, 560], 0, 180, fill='#e94560', width=2)
    elif icon_type == 'question':
        draw.arc([850, 250, 1070, 550], 180, 0, fill='#e94560', width=15)
        draw.rectangle([950, 500, 970, 650], fill='#e94560')
        draw.ellipse([920, 630, 1000, 720], fill='#e94560')
    elif icon_type == 'world':
        draw.ellipse([600, 200, 1320, 880], fill='#0f3460', outline='#e94560', width=5)
        dots = [(800, 400), (1000, 350), (1100, 500), (900, 550), (1050, 600)]
        for dx, dy in dots:
            draw.ellipse([dx-15, dy-15, dx+15, dy+15], fill='#e94560')
        for i in range(len(dots)-1):
            draw.line([dots[i], dots[i+1]], fill='#e94560', width=2)
    
    try:
        title_font = ImageFont.truetype("arial.ttf", 80)
        text_font = ImageFont.truetype("arial.ttf", 50)
    except:
        title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
    
    draw.text((960, 800), text, fill='white', font=title_font, anchor='mm')
    if subtext:
        draw.text((960, 900), subtext, fill='#e94560', font=text_font, anchor='mm')
    img.save(f'assets/{filename}')
    print(f"✅ Created: {filename}")

def main():
    create_folder()
    create_background()
    create_slide('slide1_title.png', 'HOW DOES AI LEARN?', 'The Truth About Machine Learning', 'brain')
    create_slide('slide2_chess.png', 'AI Mastered Chess in 4 Hours', 'And Beat Every Human Champion', 'chess')
    create_slide('slide3_computer.png', 'Pattern Matching', 'Finding What Makes Things Unique', 'computer')
    create_slide('slide4_pattern.png', 'MILLIONS of Examples', 'Cats: Ears, Whiskers, Tail', None)
    create_slide('slide5_three_types.png', 'THREE Ways AI Learns', 'Supervised | Unsupervised | Reinforcement', 'network')
    create_slide('slide6_neural.png', 'Neural Networks', 'Million of Tiny Decision Makers', 'network')
    create_slide('slide7_question.png', "Even Scientists Don't Understand", 'The Black Box Problem', 'question')
    create_slide('slide8_ai_world.png', 'AI is Everywhere', 'Your Phone | Your Car | Your Doctor', 'world')
    create_slide('slide9_subscribe.png', 'Subscribe for More!', 'Tech Secrets Coming Soon', None)
    print("\n🎉 All graphics created!")
    print("📁 Check the 'assets' folder!")

if __name__ == '__main__':
    main()
