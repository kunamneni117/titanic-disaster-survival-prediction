from classification_model.config.core import config
from classification_model.processing.features import ExtractLetterTransformer


def test_extract_letter_transformer(sample_input_data):
    # Given
    transformer = ExtractLetterTransformer(
        variables=config.model_config.categorical_vars_with_extraction
    )

    # When
    subject = transformer.fit_transform(sample_input_data)

    # Then
    assert len(max(subject['Cabin'].astype(str).unique(), key = len))<=4
