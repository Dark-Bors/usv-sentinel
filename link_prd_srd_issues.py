import subprocess

# Map of PRD issue numbers (parents)
prd_to_srd_map = {
    2: [8, 15, 16],                   # USV-1
    3: [9, 10, 11, 30, 31],          # USV-2
    4: [12, 13, 14, 32],             # USV-3
    5: [16, 17, 28, 33],             # USV-4
    6: [18, 20, 24, 27],             # USV-5
    7: [19, 21, 22, 23, 25, 26],     # USV-6
}

repo = "Dark-Bors/usv-sentinel"

for prd_issue, srd_issues in prd_to_srd_map.items():
    for srd_issue in srd_issues:
        cmd = [
            "gh", "issue", "edit", str(srd_issue),
            "--repo", repo,
            f"--add-parent", str(prd_issue)
        ]
        print(f"Linking SRD #{srd_issue} → PRD #{prd_issue}...")
        subprocess.run(cmd)
