import os
import shutil

def main():
    base_dir = r"c:\Users\Rajesh\Desktop\Odoo Store\project_title_uppercase\static\description"
    
    # Ensure directory exists
    os.makedirs(base_dir, exist_ok=True)
    
    # Source paths (from the AI agent's brain directory)
    src_icon = r"C:\Users\Rajesh\.gemini\antigravity-ide\brain\e5bd03e0-00b1-4325-9a1a-92c8ec6e446c\odoo_module_icon_png_1782545017370.png"
    src_cover = r"C:\Users\Rajesh\.gemini\antigravity-ide\brain\e5bd03e0-00b1-4325-9a1a-92c8ec6e446c\odoo_module_cover_png_1782545036179.png"
    
    # Destination paths
    dest_icon = os.path.join(base_dir, "icon.png")
    dest_cover = os.path.join(base_dir, "cover.png")
    
    try:
        shutil.copyfile(src_icon, dest_icon)
        print(f"[SUCCESS] Copied icon to {dest_icon}")
    except Exception as e:
        print(f"[ERROR] Failed to copy icon: {e}")
        
    try:
        shutil.copyfile(src_cover, dest_cover)
        print(f"[SUCCESS] Copied cover to {dest_cover}")
    except Exception as e:
        print(f"[ERROR] Failed to copy cover: {e}")

if __name__ == "__main__":
    main()
