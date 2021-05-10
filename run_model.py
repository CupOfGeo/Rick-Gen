import gpt_2_simple as gpt2


#gen_file = 'output.txt'

def generate_out(pre):
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name='run1')
    My_gen = gpt2.generate(sess,
                  length=200,
                  temperature=.7,
                  prefix=pre,
                  nsamples=1,
                  batch_size=1,
                  return_as_list=True,
                  )

    return My_gen[0]

#out = generate_out('Rick:')
#print(out)

