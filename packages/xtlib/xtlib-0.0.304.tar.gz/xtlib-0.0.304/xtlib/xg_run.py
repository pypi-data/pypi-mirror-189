# xg_run.py: main entry point for the xg program
import os
import sys
import openai
from xtlib import utils

prompt_prefix = '''We are going to generate command lines for a CLI tool called "xt" that help users launch jobs and generate reports and plots.  Here are some sample English commands and their XT equivalents: 

list the top 15 runs from job235 -> xt list runs job235 --sort=metrics.dev-seq_acc --last=15 
show the last 5 jobs launched -> xt list jobs --last=5 
show any errors from job271 -> xt @error_report --job=job271 
show exploratory report job281 -> xt @explore_report --job=job281 
run train.py on singularity  for 500 epochs with lr=.001 -> xt run --target=singularity  train.py --epochs=500 --lr=.001
run train.py on labcoatbatch-hi for 1000 epochs with the sgd optimizer -> xt run --target=labcoatbatch-hi train.py --epochs=1000 --optimizer=sgd
'''

def main(test_text=None):
    user_text = " ".join(sys.argv[1:])
    if not user_text:
        user_text = test_text

    #print("user_text: " + user_text)

    prompt = prompt_prefix + user_text + " ->"
    utils.set_openai_key()
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=512)

    xt_cmd = response["choices"][0]["text"].strip()
    assert xt_cmd.startswith("xt")

    print("xt_cmd: " + str(xt_cmd))
    os.system(xt_cmd)

if __name__ == "__main__":
    # test xg 
    main("run miniMnist.py on singularity for 50 epochs with lr=.001")




