#!/usr/bin/env python3
"""Generate windhawk/taskbar/dock/*.json from the canonical PALETTES.

Dock-style taskbar themes: a floating centered pill, with each palette's
accent on borders, running indicator and labels, and its `background` color
behind the pill. The Start button is hidden in every variant.

The transparent glass layout is kept as a one-off copy in glassx.json (not
touched by this script). Usage: python generate.py
"""

import importlib.util
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
GEN = os.path.join(REPO, "yasb", "generate.py")
spec = importlib.util.spec_from_file_location("yasb_gen", GEN)
yasb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(yasb)

# Order matches the yasb/zebar packs.
ORDER = ["x", "madrid", "lahabana", "miami", "paris", "tokio", "oslo", "helsinki", "berlin", "london", "praha", "bogota"]

# The differentiating accent of each palette (replaces the xdark #facc15).
ACCENTS = {
    "x": "#fce566",
    "madrid": "#990026",
    "lahabana": "#e5ff9d",
    "miami": "#ff4c8b",
    "paris": "#c4bdff",
    "tokio": "#fd9353",
    "oslo": "#4dc4ff",
    "helsinki": "#1faa9e",
    "berlin": "#cccccc",
    "london": "#333333",
    "praha": "#bd93f9",
    "bogota": "#47e6ff",
}

X_BG = "#050505"  # X is the hand-tuned base palette.

# Dock-like template (apps sit on a floating centered pill, no button boxes),
# still using $accent (borders + running indicator) and $bg (the pill fill).
DOCK_TEMPLATE = {
    "theme": "",
    "controlStyles[0].target": "Taskbar.TaskbarFrame",
    "controlStyles[0].styles[0]": "Width=Auto",
    "controlStyles[0].styles[1]": "HorizontalAlignment=Center",
    "controlStyles[0].styles[2]": "Margin=250,0,250,0",
    "controlStyles[1].target": "Taskbar.TaskbarFrame > Grid#RootGrid",
    "controlStyles[1].styles[0]": "Background:=<WindhawkBlur BlurAmount=\"18\" TintColor=\"$bg\" TintOpacity=\"0.8\" />",
    "controlStyles[1].styles[1]": "Padding=6,0,6,0",
    "controlStyles[1].styles[2]": "CornerRadius=14",
    "controlStyles[1].styles[3]": "Margin=0,0,0,10",
    "controlStyles[1].styles[4]": "BorderThickness=1",
    "controlStyles[1].styles[5]": "BorderBrush=$accent66",
    "controlStyles[2].target": "Taskbar.TaskbarFrame > Grid#RootGrid > Taskbar.TaskbarBackground > Grid > Rectangle#BackgroundFill",
    "controlStyles[2].styles[0]": "Visibility=Collapsed",
    "controlStyles[3].target": "Rectangle#BackgroundStroke",
    "controlStyles[3].styles[0]": "Visibility=Collapsed",
    "controlStyles[4].target": "Taskbar.TaskListButton",
    "controlStyles[4].styles[0]": "CornerRadius=8",
    "controlStyles[4].styles[1]": "Margin=2,6,2,4",
    "controlStyles[5].target": "Taskbar.TaskListButtonPanel > Border#BackgroundElement",
    "controlStyles[5].styles[0]": "Background=Transparent",
    "controlStyles[6].target": "Taskbar.TaskListLabeledButtonPanel > Border#BackgroundElement",
    "controlStyles[6].styles[0]": "Background=Transparent",
    "controlStyles[7].target": "Taskbar.TaskListButton > Grid > Rectangle#RunningIndicator",
    "controlStyles[7].styles[0]": "Height=4",
    "controlStyles[7].styles[1]": "RadiusX=2",
    "controlStyles[7].styles[2]": "RadiusY=2",
    "controlStyles[7].styles[3]": "Fill@ActiveNormal=$accent",
    "controlStyles[7].styles[4]": "VerticalAlignment=Bottom",
    "controlStyles[7].styles[5]": "Margin=14,0,14,2",
    "controlStyles[7].styles[6]": "StrokeThickness=0",
    "controlStyles[8].target": "Grid#SystemTrayFrameGrid",
    "controlStyles[8].styles[0]": "Background=Transparent",
    "controlStyles[8].styles[1]": "CornerRadius=10",
    "controlStyles[8].styles[2]": "Margin=0,6,4,4",
    "controlStyles[8].styles[3]": "Padding=6,0,6,0",
    "controlStyles[9].target": "SystemTray.TextIconContent > Grid#ContainerGrid > SystemTray.AdaptiveTextBlock#Base > TextBlock#InnerTextBlock",
    "controlStyles[9].styles[0]": "FontSize=13",
    "controlStyles[9].styles[1]": "Foreground=$accent",
    "controlStyles[10].target": "TextBlock#LabelControl",
    "controlStyles[10].styles[0]": "FontFamily=Segoe UI Medium",
    "controlStyles[10].styles[1]": "Foreground=$accent",
    "controlStyles[10].styles[2]": "Margin=1,0,0,0",
    "controlStyles[10].styles[3]": "VerticalAlignment=Center",
    "controlStyles[10].styles[4]": "TextWrapping=NoWrap",
    "controlStyles[11].target": "Taskbar.ExperienceToggleButton#LaunchListButton[AutomationProperties.AutomationId=StartButton]",
    "controlStyles[11].styles[0]": "Visibility=Collapsed",
    "controlStyles[12].target": "SystemTray.TextIconContent > Grid#ContainerGrid > SystemTray.AdaptiveTextBlock#Base > TextBlock#InnerTextBlock",
    "controlStyles[12].styles[0]": "FontSize=16",
    "controlStyles[12].styles[1]": "Foreground=$accent",
}


def with_alpha(color, alpha):
    return color.lower().replace("#", "#" + alpha, 1)


def main():
    dock_dir = os.path.join(HERE, "dock")
    os.makedirs(dock_dir, exist_ok=True)

    for pid in ORDER:
        accent = ACCENTS[pid]
        bg = X_BG if pid == "x" else yasb.PALETTES[pid]["background"]
        ctx = {
            "$accent40": with_alpha(accent, "40"),
            "$accent66": with_alpha(accent, "66"),
            "$accent": accent,
            "$bg": bg,
        }
        data = dict(DOCK_TEMPLATE)
        for token, color in ctx.items():
            data = {key: value.replace(token, color) for key, value in data.items()}
        path = os.path.join(dock_dir, "{}.json".format(pid))
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
            f.write("\n")
        print("wrote", path, "accent", accent, "bg", bg)


if __name__ == "__main__":
    main()
