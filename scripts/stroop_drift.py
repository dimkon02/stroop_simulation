def stroop_drift(color_signal, word_signal, color_weight, word_weight):
    """
    Computes the drift rate for a Stroop trial.
    
    Parameters:
        color_signal: +1 or -1 (correct color)
        word_signal: +1 or -1 (word meaning)
        color_weight: weight for color info
        word_weight: weight for word interference
    Returns:
        float: drift rate
    """
    return color_weight * color_signal + word_weight * word_signal