CUDA_VISIBLE_DEVICES=1 python run_seq2seq.py \
    --model_name_or_path t5_model/t5-base \
    --model_name t5-base \
    --do_train \
    --do_eval \
    --train_file data/docomo_data/train.json \
    --validation_file data/docomo_data/dev.json \
    --source_prefix "summarize: " \
    --output_dir /checkpoint/docomo \
    --overwrite_output_dir \
    --per_device_train_batch_size=8 \
    --per_device_eval_batch_size=8 \
    --predict_with_generate \
	--eval_steps=50 \
    --logging_steps=50 \
    --num_train_epochs=3.0 \
    --learning_rate=1e-4 \
    --num_beams=1 \
    --evaluation_strategy epoch \
    --save_strategy epoch \
    --load_best_model_at_end True \