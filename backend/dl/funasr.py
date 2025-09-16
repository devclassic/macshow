from modelscope.hub.snapshot_download import snapshot_download

model_repos = {
    "paraformer-zh": "iic/speech_seaco_paraformer_large_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
    "fsmn-vad": "iic/speech_fsmn_vad_zh-cn-16k-common-pytorch",
    "ct-punc": "iic/punc_ct-transformer_cn-en-common-vocab471067-large",
    "cam++": "iic/speech_campplus_sv_zh-cn_16k-common",
}

for model_name, repo_id in model_repos.items():
    snapshot_download(
        repo_id,
        local_dir=f"./models/funasr/{model_name}",
    )
