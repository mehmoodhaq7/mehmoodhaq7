import sys
import math
from PIL import Image

def build_svg(is_dark, ascii_lines_svg):
    bg_col = "#161b22" if is_dark else "#f6f8fa"  
    text_col = "#c9d1d9" if is_dark else "#24292f"
    key_col = "#ffa657" if is_dark else "#bc4c00"
    val_col = "#a5d6ff" if is_dark else "#0550ae"
    add_col = "#3fb950" if is_dark else "#2da44e"
    del_col = "#f85149" if is_dark else "#cf222e"
    cc_col = "#616e7f" if is_dark else "#6e7781"

    svg_header = f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="985px" height="530px" font-size="15px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
.key {{fill: {key_col};}}
.value {{fill: {val_col};}}
.addColor {{fill: {add_col};}}
.delColor {{fill: {del_col};}}
.cc {{fill: {cc_col};}}
text, tspan {{white-space: pre;}}
</style>
<rect width="985px" height="530px" fill="{bg_col}" rx="15"/>
<text x="15" y="30" font-family="monospace">
"""
    for i, line in enumerate(ascii_lines_svg):
        y_pos = 30 + i * 20 
        svg_header += f'<tspan x="15" y="{y_pos}" xml:space="preserve">{line}</tspan>\n'
        
    svg_header += '</text>\n'
    
    right_content = f"""<text x="410" y="30" fill="{text_col}">
<tspan x="410" y="30">mehmood@haq</tspan> <tspan class="cc">-————————————————————————————————————————————————————————-—-</tspan>
<tspan x="410" y="50" class="cc">. </tspan><tspan class="key">OS</tspan>:<tspan class="cc"> ........................ </tspan><tspan class="value">Linux, macOS, Windows</tspan>
<tspan x="410" y="70" class="cc">. </tspan><tspan class="key">Kernel</tspan>:<tspan class="cc"> .................... </tspan><tspan class="value">DevOps &amp; Cloud Engineer</tspan>
<tspan x="410" y="90" class="cc">. </tspan><tspan class="key">Uptime</tspan>:<tspan class="cc"> .................... </tspan><tspan class="value">5 Years (Tech Field)</tspan>
<tspan x="410" y="110" class="cc">. </tspan><tspan class="key">Location</tspan>:<tspan class="cc"> .................. </tspan><tspan class="value">Lahore, Pakistan</tspan>
<tspan x="410" y="130" class="cc">. </tspan><tspan class="key">Certifications</tspan>:<tspan class="cc"> ............ </tspan><tspan class="value">AWS Certified Solutions Architect</tspan>
<tspan x="410" y="150" class="cc">. </tspan>
<tspan x="410" y="170" class="cc">. </tspan><tspan class="key">Skills</tspan>.<tspan class="key">Cloud</tspan>:<tspan class="cc"> .............. </tspan><tspan class="value">AWS (EC2, EKS, RDS, VPC, Lambda)</tspan>
<tspan x="410" y="190" class="cc">. </tspan><tspan class="key">Skills</tspan>.<tspan class="key">Containers</tspan>:<tspan class="cc"> ......... </tspan><tspan class="value">Docker, Kubernetes, Helm, ArgoCD</tspan>
<tspan x="410" y="210" class="cc">. </tspan><tspan class="key">Skills</tspan>.<tspan class="key">IaC</tspan>:<tspan class="cc"> ................. </tspan><tspan class="value">Terraform, HCL</tspan>
<tspan x="410" y="230" class="cc">. </tspan><tspan class="key">Skills</tspan>.<tspan class="key">Pipelines</tspan>:<tspan class="cc"> ........... </tspan><tspan class="value">Jenkins, GitHub Actions, GitLab CI</tspan>
<tspan x="410" y="250" class="cc">. </tspan><tspan class="key">Skills</tspan>.<tspan class="key">Security</tspan>:<tspan class="cc"> ............ </tspan><tspan class="value">SonarQube, Trivy, Vault</tspan>
<tspan x="410" y="270" class="cc">. </tspan><tspan class="key">Skills</tspan>.<tspan class="key">Observability</tspan>:<tspan class="cc"> ....... </tspan><tspan class="value">Prometheus, Loki, Grafana</tspan>
<tspan x="410" y="290" class="cc">. </tspan><tspan class="key">Skills</tspan>.<tspan class="key">Languages</tspan>:<tspan class="cc"> ........... </tspan><tspan class="value">Python, JavaScript, TypeScript, Bash</tspan>
<tspan x="410" y="310" class="cc">. </tspan>
<tspan x="410" y="330">- Contact </tspan><tspan class="cc">-——————————————————————————————————————————————————————————-—-</tspan>
<tspan x="410" y="350" class="cc">. </tspan><tspan class="key">Email</tspan>:<tspan class="cc"> ..................... </tspan><tspan class="value">mehmoodulhaq97@gmail.com</tspan>
<tspan x="410" y="370" class="cc">. </tspan><tspan class="key">LinkedIn</tspan>:<tspan class="cc"> .................. </tspan><tspan class="value">mehmoodhaq</tspan>
<tspan x="410" y="390" class="cc">. </tspan>
<tspan x="410" y="410" class="cc">. </tspan>
<tspan x="410" y="430">- GitHub Stats </tspan><tspan class="cc">-—————————————————————————————————————————————————————-—-</tspan>
<tspan x="410" y="450" class="cc">. </tspan><tspan class="key">Repos</tspan>:<tspan class="cc"> .... </tspan><tspan class="value">27</tspan> {{<tspan class="key">Contributed</tspan>: <tspan class="value">30</tspan>}} | <tspan class="key">Stars</tspan>:<tspan class="cc"> ........... </tspan><tspan class="value">0</tspan>
<tspan x="410" y="470" class="cc">. </tspan><tspan class="key">Commmits</tspan>:<tspan class="cc"> ................. </tspan><tspan class="value">1,532</tspan> | <tspan class="key">Followers</tspan>:<tspan class="cc"> ....... </tspan><tspan class="value">69</tspan>
<tspan x="410" y="490" class="cc">. </tspan><tspan class="key">Lines of Code on GitHub</tspan>:<tspan class="cc">. </tspan><tspan class="value">42,912</tspan> ( <tspan class="addColor">49,102</tspan><tspan class="addColor">++</tspan>, <tspan id="loc_del_dots"> </tspan><tspan class="delColor">6,190</tspan><tspan class="delColor">--</tspan> )
<tspan x="410" y="510" class="cc">. </tspan>
</text>
</svg>
"""
    return svg_header + right_content

def generate_svg(image_path, output_dark, output_light):
    print("Opening Image...", image_path)
    img = Image.open(image_path).convert("RGB")
    
    target_w = 44
    target_h = 25
    
    target_aspect = (44 * 9.0) / (25 * 20.0)
    w, h = img.size
    img_aspect = w / h
    
    if img_aspect > target_aspect:
        new_w = int(h * target_aspect)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target_aspect)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))
        
    img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    pixels = img.load()
    
    ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    
    ascii_lines_svg = []
    
    for y in range(target_h):
        line_elements = []
        for x in range(target_w):
            
            # Simple fade ONLY on the Top-Left and Top-Right corners
            dx_left = x * 9.0
            dx_right = (target_w - 1 - x) * 9.0
            dy = y * 20.0  # y is distance from top
            
            dist_tl = math.sqrt(dx_left**2 + dy**2)
            dist_tr = math.sqrt(dx_right**2 + dy**2)
            
            dist_corner = min(dist_tl, dist_tr)
            
            fade_radius = 160.0 # Only affects the extreme top corners
            
            if dist_corner < fade_radius:
                # The closer it is to 0 (the absolute corner), the closer factor is to 0
                factor = dist_corner / fade_radius
                # Smooth curve easing
                factor = factor * factor * (3 - 2 * factor)
            else:
                # Everything else remains safely untouched at 100% visibility
                factor = 1.0
                
            if factor < 0.05:
                line_elements.append(' ')
                continue
                
            r, g, b = pixels[x, y]
            brightness = sum([r,g,b])/3
            
            char_idx = int((brightness / 255.0) * (len(ascii_chars) - 1))
            char_idx = max(0, min(len(ascii_chars)-1, char_idx))
            char = ascii_chars[char_idx]
            
            if char in ["<", ">", "&", '"', "'"]:
                char = {"<": "&lt;", ">": "&gt;", "&": "&amp;", '"': "&quot;", "'": "&apos;"}[char]
            
            L = int(0.299 * r + 0.587 * g + 0.114 * b)
            hex_color = f"#{L:02x}{L:02x}{L:02x}"
            
            if factor < 0.99:
                line_elements.append(f'<tspan fill="{hex_color}" fill-opacity="{factor:.2f}">{char}</tspan>')
            else:
                line_elements.append(f'<tspan fill="{hex_color}">{char}</tspan>')

        ascii_lines_svg.append("".join(line_elements))

    print("Writing files...")
    with open(output_dark, 'w', encoding='utf-8') as f:
        f.write(build_svg(True, ascii_lines_svg))
    with open(output_light, 'w', encoding='utf-8') as f:
        f.write(build_svg(False, ascii_lines_svg))

if __name__ == "__main__":
    generate_svg(r"C:\Users\mehmoodhaq\.gemini\antigravity\brain\f6d67183-38a7-4141-a5ca-259b755ea5b9\media__1775752206218.png", 
                 "dark_mode.svg",
                 "light_mode.svg")
    print("Success")
