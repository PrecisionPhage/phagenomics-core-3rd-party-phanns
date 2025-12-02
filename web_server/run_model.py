import Phanns_f
import ann_config
import sys
import os

# Usage: python run_model.py <input.faa> [output_dir]
# If output_dir is provided, CSV will be written there instead of current directory

input_file = sys.argv[1]
output_dir = sys.argv[2] if len(sys.argv) > 2 else None

test=Phanns_f.ann_result(input_file, output_dir=output_dir)
(names,pp)=test.predict_score_single_run()
print(pp)
