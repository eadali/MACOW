from .yacs import CfgNode

cfg = CfgNode(new_allowed=True)
cfg.save_dir = "./"

# System configuration
cfg.system = CfgNode(new_allowed=True)
cfg.system.detector = CfgNode(new_allowed=True)
cfg.system.detector.thresholds = CfgNode(new_allowed=True)
cfg.system.detector.slicing = CfgNode(new_allowed=True)
# Tracker configuration
cfg.system.tracker = CfgNode(new_allowed=True)


def load_config(cfg, args_cfg):
    cfg.defrost()
    cfg.merge_from_file(args_cfg)
    cfg.freeze()


if __name__ == "__main__":
    import sys

    with open(sys.argv[1], "w") as f:
        print(cfg, file=f)
