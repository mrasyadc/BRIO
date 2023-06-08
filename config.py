def cnndm_setting(args):
    # default setting for cnndm
    args.batch_size = getattr(args, 'batch_size', 1)
    args.epoch = getattr(args, 'epoch', 100)
    args.report_freq = getattr(args, "report_freq", 100)
    args.accumulate_step = getattr(args, "accumulate_step", 16)
    args.margin = getattr(args, "margin", 0.001)
    args.gold_margin = getattr(args, "gold_margin", 0)
    args.gold_weight = getattr(args, "gold_weight", 0)
    args.mle_weight = getattr(args, "mle_weight", 0.1)
    args.rank_weight = getattr(args, "rank_weight", 10)
    args.model_type = getattr(args, "model_type", "facebook/bart-large-cnn")
    args.warmup_steps = getattr(args, "warmup_steps", 10000)
    args.normalize = getattr(args, "normalize", True)
    args.grad_norm = getattr(args, "grad_norm", 0)
    args.seed = getattr(args, "seed", 970903)
    args.no_gold = getattr(args, "no_gold", False)
    args.pretrained = getattr(args, "pretrained", None)
    args.max_lr = getattr(args, "max_lr", 2e-3)
    args.scale = getattr(args, "scale", 1)
    args.score_mode = getattr(args, "score_mode", "log")
    args.datatype = getattr(args, "datatype", "diverse")
    args.dataset = getattr(args, "dataset", "cnndm")
    args.max_len = getattr(args, "max_len", 114)
    args.max_num = getattr(args, "max_num", 4)
    args.smooth = getattr(args, "smooth", 0.1)
    args.total_len = getattr(args, "total_len", 265)
    args.length_penalty = getattr(args, "length_penalty", 2.0)
    args.do_sample = getattr(args, "do_sample", True)
    args.gen_max_len = getattr(args, "gen_max_len", 114)
    args.gen_min_len = getattr(args, "gen_min_len", 1)
    args.is_pegasus = getattr(args, "is_pegasus", False)
    args.adding = getattr(args, "adding", 0)
    args.eval_interval = getattr(args, "eval_interval", 1000)
    args.num_beams = getattr(args, "num_beams", 4)

def xsum_setting(args):
    # default setting for xsum
    args.batch_size = getattr(args, 'batch_size', 2)
    args.epoch = getattr(args, 'epoch', 100)
    args.report_freq = getattr(args, "report_freq", 1)
    args.accumulate_step = getattr(args, "accumulate_step", 4)
    args.margin = getattr(args, "margin", 0.001)
    args.gold_margin = getattr(args, "gold_margin", 0)
    args.gold_weight = getattr(args, "gold_weight", 0)
    args.mle_weight = getattr(args, "mle_weight", 0.1)
    args.rank_weight = getattr(args, "rank_weight", 10)
    args.model_type = getattr(args, "model_type", "google/pegasus-xsum")
    args.warmup_steps = getattr(args, "warmup_steps", 10000)
    args.normalize = getattr(args, "normalize", True)
    args.grad_norm = getattr(args, "grad_norm", 0)
    args.seed = getattr(args, "seed", 970903)
    args.no_gold = getattr(args, "no_gold", False)
    args.pretrained = getattr(args, "pretrained", None)
    args.max_lr = getattr(args, "max_lr", 2e-3)
    args.scale = getattr(args, "scale", 0.01)
    args.score_mode = getattr(args, "score_mode", "log")
    args.datatype = getattr(args, "datatype", "diverse")
    args.dataset = getattr(args, "dataset", "xsum")
    args.max_len = getattr(args, "max_len", 80)
    args.max_num = getattr(args, "max_num", 16)
    args.smooth = getattr(args, "smooth", 0.1)
    args.total_len = getattr(args, "total_len", 512)
    args.length_penalty = getattr(args, "length_penalty", 0.6)
    args.do_sample = getattr(args, "do_sample", True)
    args.gen_max_len = getattr(args, "gen_max_len", 45)
    args.gen_min_len = getattr(args, "gen_min_len", 1)
    args.is_pegasus = getattr(args, "is_pegasus", True)
    args.adding = getattr(args, "adding", 0)
    args.eval_interval = getattr(args, "eval_interval", 1000)
    args.num_beams = getattr(args, "num_beams", 8)