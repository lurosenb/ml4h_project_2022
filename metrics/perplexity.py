from evaluate import load

def mean_perplexity(predictions):
    perplexity = load("perplexity", module_type="metric")
    results = perplexity.compute(predictions=predictions, model_id='gpt2')
    return round(results['mean_perplexity'],3)