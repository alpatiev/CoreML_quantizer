import os
import sys
import coremltools

def quantize_coreml_model(model_name, quantized_model_name, bitwidth=8):
    try:
        model_path = f"{model_name}.mlmodel"
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Error: Input model file '{model_path}' not found.")
        print(f">>> Start processing for {bitwidth}-bit quantization.")
        model = coremltools.models.MLModel(model_path)
        quantized_model = coremltools.models.neural_network.quantization_utils.quantize_weights(model, nbits=bitwidth)
        quantized_model.save(f"{quantized_model_name}.mlmodel")
        print(f">>> Quantization complete. Quantized model saved at: {quantized_model_name}.mlmodel")
    except Exception as e:
        print(f">>> Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(">>> Error: Incorrect number of parameters. Please provide the input model name, the output quantized model name, and the quantization value (8 or 16).")
    else:
        original_model_name = sys.argv[1]
        quantized_model_name = sys.argv[2]
        if original_model_name.endswith('.mlmodel') or quantized_model_name.endswith('.mlmodel'):
            print(">>> Error: Input and output model names must not have the '.mlmodel' extension.")
            sys.exit(1)
        try:
            quantized_bitwidth = int(sys.argv[3])
            if quantized_bitwidth not in [8, 16]:
                raise ValueError("Quantization value must be 8 or 16.")
        except ValueError:
            print(">>> Error: Invalid quantization value. Please provide 8 or 16.")
            sys.exit(1)
        quantize_coreml_model(original_model_name, quantized_model_name, bitwidth=quantized_bitwidth)
