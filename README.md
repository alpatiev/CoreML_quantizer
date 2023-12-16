# About

This repository contains a Python script for quantizing Core ML models which helps reduce their memory footprint and improve inference speed.
Quantization usually tends to lower model accuracy, don't forget it.

## Requirements

The `quantizer.py` script uses python 3 and above and the `coremltools` library

```bash
pip install coremltools
```

## Usage

### 1. Clone the repository:

```bash
git clone https://github.com/alpatiev/CoreML_quiantizer
```

### 2. Navigate to the script directory and move the .mlmodel file to the same path:

```bash
cd CoreML_quantizer
```

### 3. Run the script from the command line with the following parameters:

```bash
python quantize_coreml_model.py <original_model_name> <quantized_model_name> <quantization_bitwidth>
```

`<original_model_name>: The name of the original Core ML model (without the .mlmodel extension).`
`<quantized_model_name>: The desired name for the quantized model (without the .mlmodel extension).`
`<quantization_bitwidth>: The bitwidth for quantization (8 or 16).`



