import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFilter , ImageSequence 
from itertools import cycle
import cv2
import webbrowser

class CyberSecurityAwarenessPoster:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Cybersecurity Awareness Poster")
        self.root.geometry("1180x1200")
        self.root.configure(bg='#333333')  
        self.add_blurred_background('img/headimg.jpg', (1200, 1000))
        self.add_footer()
        self.add_heading_and_images()
        self.add_content_rows()
        self.add_video_canvas('Cyber Security - Video Animation Services.mp4', size=(600, 400))
        self.add_side_gifs('img/gif1.gif', 'img/gif2.webp')
    
    def add_side_gifs(self, left_gif_path, right_gif_path):
        # Left GIF
        self.add_gif(left_gif_path, x=40, y=650)  # Adjust x and y according to where you want the GIF
        
        # Right GIF
        self.add_gif(right_gif_path, x=930, y=645)  # Adjust x and y according to where you want the GIF

    def add_gif(self, gif_path, x, y):
        gif = Image.open(gif_path)
        frames = [ImageTk.PhotoImage(img.resize((200, 200), Image.LANCZOS)) for img in ImageSequence.Iterator(gif)]

        gif_label = tk.Label(self.root, bg='#2E2E2E')
        gif_label.place(x=x, y=y)

        self.update_gif(gif_label, frames, 0)

    def update_gif(self, label, frames, frame_index):
        frame = frames[frame_index]
        label.config(image=frame)
        next_frame_index = (frame_index + 1) % len(frames)  # Loop back to first frame
        # Adjust the delay as needed. 100 milliseconds is an example.
        self.root.after(100, self.update_gif, label, frames, next_frame_index)


    def add_blurred_background(self, path, window_size):
        background_image = ImageUtils.create_blurred_background(path, window_size)
        background_label = tk.Label(self.root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image

    def add_footer(self):
        Footer(self.root)

    def add_heading_and_images(self):
        HeadingAndImages(self.root)

    def add_content_rows(self):
        ContentRows(self.root)

    def add_video_canvas(self, video_path, size=None):
        VideoPlayer(self.root, video_path, size=size)
    
    def add_side_images(self, left_image_path, right_image_path):
        # Left image
        left_photo = ImageUtils.create_circle_image(left_image_path, (100, 100))
        left_label = tk.Label(self.root, image=left_photo, bg='white')
        left_label.image = left_photo
        left_label.place(x=100, y=680)  # Adjust x and y according to where you want the image
        
        # Right image
        right_photo = ImageUtils.create_circle_image(right_image_path, (100, 100))
        right_label = tk.Label(self.root, image=right_photo, bg='white')
        right_label.image = right_photo
        right_label.place(x=960, y=680)  # Adjust x and y according to where you want the image

class ImageUtils:
    @staticmethod
    def create_blurred_background(path, window_size):
        try:
            img = Image.open(path)
            if img.mode not in ('RGB', 'L'):
                img = img.convert('RGB')
            img = img.resize(window_size, Image.Resampling.LANCZOS)
            blurred_img = img.filter(ImageFilter.GaussianBlur(15))
            return ImageTk.PhotoImage(blurred_img)
        except FileNotFoundError as e:
            print(f"Error: File {path} not found. {e}")
            exit()

    @staticmethod
    def create_circle_image(path, size):
        try:
            img = Image.open(path).resize(size, Image.Resampling.LANCZOS)
            mask = Image.new('L', size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + size, fill=255)
            result = Image.new('RGBA', size, (0, 0, 0, 0))
            result.paste(img, (0, 0), mask)
            return ImageTk.PhotoImage(result)
        except FileNotFoundError as e:
            print(f"Error: File {path} not found. {e}")
            exit()

class HeadingAndImages:
    def __init__(self, root):
        self.root = root
        self.create_heading_and_images()

    def create_heading_and_images(self):
        frame = tk.Frame(self.root, bg='white')
        frame.pack(expand=True, fill='both')

        try:
            left_photo = ImageUtils.create_circle_image('img/headimg.jpg', (100, 100))  # Assuming ImageUtils handles conversion to tk.PhotoImage
            right_photo = ImageUtils.create_circle_image('img/headimg.jpg', (100, 100))  # and cropping to a circle
        except Exception as e:
            print(f"Failed to load images: {e}")
            exit()

        left_label = tk.Label(frame, image=left_photo, bg='white')
        left_label.image = left_photo  # Keep a reference so it's not garbage collected
        left_label.grid(row=0, column=0, padx=50)

        heading_text = "Digital Crime Awareness\nTips & Insights from Ramnarain Ruia College's CS Department"
        heading_label = tk.Label(frame, text=heading_text, font=('Arial', 18, 'bold'), bg='white', justify=tk.CENTER)
        heading_label.grid(row=0, column=1, padx=10)  # Adjusted padx for potentially longer text

        right_label = tk.Label(frame, image=right_photo, bg='white')
        right_label.image = right_photo  # Keep a reference
        right_label.grid(row=0, column=2, padx=80)

class ContentRows:
    def __init__(self, root):
        self.root = root
        self.create_content_rows()

    def create_content_rows(self):
        row_contents = [
            ("Use Strong Passwords", "Create complex passwords that are hard to guess and use a different  \n password for each of your accounts. Consider using a password manager to keep  \n track of your passwords securely."),
            ("Two-Factor Authentication", "Whenever possible, enable 2FA on your accounts. \n This adds an extra layer of security by requiring a second form of verification beyond  \n just your password."),
            ("Keep Your Software Updated", "Regularly update your operating system,  \n browsers, and applications.These updates often contain patches for  \n security vulnerabilities that have been discovered since the last update."),
            ("Use Secure Networks", "Avoid using public Wi-Fi networks for sensitive activities. Consider  \n using a Virtual Private Network (VPN) to encrypt your internet \n connection and protect your data from prying eyes."),
            ("Backup and Recovery", "Ensure that you have regular backups of important data. \n This can be a lifesaver in case of data loss due to malware attacks, hardware failures, or \n accidental deletions."),
        ]

        image_paths = [
            "img/img1.png",
            "img/img2.jpg",
            "img/img3.png",
            "img/img4.jpg",
            "img/img5.png"
        ]

        heading_colors = cycle(["#00A1E4", "#00A1E4", "#00A1E4", "#00A1E4", "#00A1E4"])

        side_positions = cycle(['left', 'right'])  # Alternating positions

        for (heading, content), image_path, color, position in zip(row_contents, image_paths, heading_colors, side_positions):
            self.add_content_row(heading, content, image_path, color, position)

    def add_content_row(self, heading, content, image_path, color, position):
        # Here we add highlightbackground and highlightthickness to create a border
        frame = tk.Frame(self.root, bg='white', highlightbackground="black", highlightthickness=2)  # Added border here
        frame.pack(fill='x', pady=5, padx=10)  # Added padx for consistent padding around borders

        img_photo = ImageUtils.create_circle_image(image_path, (60, 60))
        img_label = tk.Label(frame, image=img_photo, bg='white')
        img_label.image = img_photo

        content_frame = tk.Frame(frame, bg='white')
        content_frame.pack(side=position, expand=True, fill='both', padx=20)

        if position == 'left':
            img_label.pack(side='left', padx=20)
        else:
            img_label.pack(side='right', padx=20)

        heading_label = tk.Label(content_frame, text=heading, font=('Arial', 16, 'bold'), fg=color, bg='white')
        content_label = tk.Label(content_frame, text=content, font=('Arial', 14), bg='white')

        heading_label.grid(row=0, column=0, sticky='w')
        content_label.grid(row=0, column=1, sticky='w', padx=10)  # Add some padding between heading and content

        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=3)



class VideoPlayer:
    def __init__(self, root, video_path, size=None):
        self.root = root
        self.video_path = video_path
        self.size = size if size is not None else (640, 480)
        self.create_video_canvas()

    def create_video_canvas(self):
        self.canvas = tk.Canvas(self.root, width=self.size[0], height=self.size[1], bg='black')
        
        # The video canvas will now be placed in the center when packed with expand=True
        self.canvas.pack(expand=True)
        
        self.capture = cv2.VideoCapture(self.video_path)
        self.update_video_frame()

    def update_video_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, self.size)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(self.size[0] // 2, self.size[1] // 2, image=self.photo, anchor=tk.CENTER)
            self.root.after(15, self.update_video_frame)
        else:
            # Loop the video
            self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
            self.update_video_frame()

class Footer:
    def __init__(self, root):
        self.root = root
        self.create_footer()

    def create_footer(self):
        footer_frame = tk.Frame(self.root, bg='#2E2E2E', height=100)  # Darker footer for contrast
        footer_frame.pack(fill='x', side='bottom')

        logo_photo = ImageUtils.create_circle_image('img/ruia.png', (40, 40))
        logo_label = tk.Label(footer_frame, image=logo_photo, bg='#2E2E2E')
        logo_label.image = logo_photo
        logo_label.pack(side='left', padx=10)

        address_label = tk.Label(footer_frame, text="L. Napoo Road, Matunga East, Mumbai, Maharashtra 400019", bg='#2E2E2E', fg='white', font=('Arial', 12))
        address_label.pack(side='left', padx=20)

        self.add_social_media_icons(footer_frame)

    def add_social_media_icons(self, footer_frame):
        social_media_icons = [
        ('img/facebook_icon.png', 'https://www.facebook.com/theruiaite/'),
        ('img/instagram_icon.png', 'https://www.instagram.com/theruiaite/?hl=en'),
        ('img/linked_icon.png', 'https://www.linkedin.com/school/ramnarain-ruia-college-mumbai/?originalSubdomain=in'),
    ]

        for icon, url in social_media_icons:
           img = Image.open(icon).resize((30, 30), Image.Resampling.LANCZOS)  # Corrected here
           photo = ImageTk.PhotoImage(img)
           btn = tk.Button(footer_frame, image=photo, command=lambda url=url: self.open_url(url), bg='#2E2E2E', borderwidth=0)
           btn.image = photo
           btn.pack(side='right', padx=10)


    @staticmethod
    def open_url(url):
        webbrowser.open_new_tab(url)


def main():
    root = tk.Tk()
    app = CyberSecurityAwarenessPoster(root)
    root.mainloop()

if __name__ == "__main__":
    main()
