__all__ = [
    'field_spec',
    'task_spec',
    'template_builder',
    'view_spec',

    'Project',
    'ClassicViewSpec',
    'TemplateBuilderViewSpec',
    'BooleanSpec',
    'StringSpec',
    'IntegerSpec',
    'FloatSpec',
    'UrlSpec',
    'FileSpec',
    'CoordinatesSpec',
    'JsonSpec',
    'ArrayBooleanSpec',
    'ArrayStringSpec',
    'ArrayIntegerSpec',
    'ArrayFloatSpec',
    'ArrayUrlSpec',
    'ArrayFileSpec',
    'ArrayCoordinatesSpec',
    'LocalizationConfig',
    'AdditionalLanguage',
]

import datetime
from enum import unique
from typing import Optional, Dict, List

from . import field_spec
from . import task_spec
from . import template_builder
from . import view_spec

from ..primitives.base import BaseTolokaObject
from ..project.field_spec import (
    BooleanSpec,
    StringSpec,
    IntegerSpec,
    FloatSpec,
    UrlSpec,
    FileSpec,
    CoordinatesSpec,
    JsonSpec,
    ArrayBooleanSpec,
    ArrayStringSpec,
    ArrayIntegerSpec,
    ArrayFloatSpec,
    ArrayUrlSpec,
    ArrayFileSpec,
    ArrayCoordinatesSpec,
)
from ..project.localization import LocalizationConfig, AdditionalLanguage
from ..project.view_spec import ClassicViewSpec, TemplateBuilderViewSpec
from ..project.task_spec import TaskSpec
from ..quality_control import QualityControl
from ...util._codegen import attribute
from ...util._extendable_enum import ExtendableStrEnum


class Project(BaseTolokaObject):
    """Top-level object in Toloka. All other entities are contained in some project.

    Describes one type of task from the requester's point of view. For example: one project can describe image segmentation,
    another project can test this segmentation. The easier the task, the better the results. If your task contains more
    than one question, it may be worth dividing it into several projects.

    In a project, you set properties for tasks and responses:
    * Input data parameters. These parameters describe the objects to display in a task, such as images or text.
    * Output data parameters. These parameters describe Tolokers' responses. They are used for validating the
        responses entered: the data type (integer, string, etc.), range of values, string length, and so on.
    * Task interface. To learn how to define the appearance of tasks, see [Task interface](https://toloka.ai/en/docs/en/guide/concepts/spec).

    Pools and training pools are related to a project.

    Attributes:
        public_name: Name of the project. Visible to Tolokers.
        public_description: Description of the project. Visible to Tolokers.
        public_instructions: Instructions for completing the task. You can use any HTML markup in the instructions.
        private_comment: Comments about the project. Visible only to the requester.
        task_spec: Parameters for input and output data and the task interface.
        assignments_issuing_type: How to assign tasks. The default value is AUTOMATED.
        assignments_automerge_enabled: Solve merging identical tasks in the project.
        max_active_assignments_count: The number of task suites a Toloker can complete simultaneously (“Active” status)
        quality_control: The quality control rule.
        metadata: Additional information about project.
        status: Project status.
        created: The UTC date and time the project was created.
        id: Project ID (assigned automatically).
        public_instructions: Instructions for completing tasks. You can use any HTML markup in the instructions.
        private_comment: Comment on the project. Available only to the customer.

    Example:
        How to create a new project.

        >>> toloka_client = toloka.TolokaClient(your_token, 'PRODUCTION')
        >>> new_project = toloka.project.Project(
        >>>     public_name='My best project!!!',
        >>>     public_description='Look at the instruction and do it well',
        >>>     public_instructions='Describe your task for Tolokers here!',
        >>>     task_spec=toloka.project.task_spec.TaskSpec(
        >>>         input_spec={'image': toloka.project.field_spec.UrlSpec()},
        >>>         output_spec={'result': toloka.project.field_spec.StringSpec(allowed_values=['OK', 'BAD'])},
        >>>         view_spec=verification_interface_prepared_before,
        >>>     ),
        >>> )
        >>> new_project = toloka_client.create_project(new_project)
        >>> print(new_project.id)
        ...
    """

    @unique
    class AssignmentsIssuingType(ExtendableStrEnum):
        """How to assign tasks:

        Attributes:
            AUTOMATED: A Toloker is assigned a task suite from the pool. You can configure the order
                for assigning task suites.
            MAP_SELECTOR: A Toloker chooses a task suite on the map. If you are using MAP_SELECTOR,
                specify the text to display in the map by setting assignments_issuing_view_config.
        """

        AUTOMATED = 'AUTOMATED'
        MAP_SELECTOR = 'MAP_SELECTOR'

    @unique
    class ProjectStatus(ExtendableStrEnum):
        """Project status:

        Attributes:
            ACTIVE: A project is active
            ARCHIVED: A project is archived
        """

        ACTIVE = 'ACTIVE'
        ARCHIVED = 'ARCHIVED'

    class AssignmentsIssuingViewConfig(BaseTolokaObject):
        """How the task will be displayed on the map

        Used only then assignments_issuing_type == MAP_SELECTOR

        Attributes:
            title_template: Name of the task. Tolokers will see it in the task preview mode.
            description_template: Brief description of the task. Tolokers will see it in the task preview mode.
        """

        @unique
        class MapProvider(ExtendableStrEnum):
            """Map provider for assignments_issuing_view_config:

            Attributes:
                YANDEX: Use Yandex Maps as a map provider
                GOOGLE: Use Google Maps as a map provider
            """

            YANDEX = 'YANDEX'
            GOOGLE = 'GOOGLE'

        title_template: str
        description_template: str
        map_provider: Optional[MapProvider] = None

    QualityControl = QualityControl

    public_name: str  # public
    public_description: str  # public
    task_spec: TaskSpec  # public
    assignments_issuing_type: AssignmentsIssuingType = attribute(default=AssignmentsIssuingType.AUTOMATED,
                                                                 required=True,
                                                                 autocast=True)  # AssignmentsIssuingType  # public

    assignments_issuing_view_config: AssignmentsIssuingViewConfig
    assignments_automerge_enabled: bool
    max_active_assignments_count: int
    quality_control: QualityControl

    metadata: Dict[str, List[str]]
    status: ProjectStatus = attribute(readonly=True)
    created: datetime.datetime = attribute(readonly=True)

    id: str = attribute(readonly=True)

    public_instructions: str  # public
    private_comment: str
    localization_config: LocalizationConfig

    def __attrs_post_init__(self):
        # TODO: delegate this check to API
        if self.assignments_issuing_type == Project.AssignmentsIssuingType.MAP_SELECTOR:
            assert self.assignments_issuing_view_config is not None

    def set_default_language(self, language: str):
        """Sets the source language used in the fields public_name, public_description, and public_instructions.

        You must set the default language if you want to use the translation in the project to other languages.
        Args:
            language: The source language.
        """
        if self.localization_config is None:
            self.localization_config = LocalizationConfig()
        self.localization_config.default_language = language

    def add_requester_translation(self, language: str, public_name: Optional[str] = None, public_description: Optional[str] = None, public_instructions: Optional[str] = None):
        """Add new translations to other language.

        You can call it several times for different languages.
        If you call it for the same language, it overwrites new values, but don't overwrite values, that you don't pass.

        Args:
            language (str): Target language. A string from ISO 639-1.
            public_name (str): Translation of the project name.
            public_description (str): Translation of the project description.
            public_instructions (str): Translation of instructions for completing tasks.

        Examples:
            How to add russian translation to the project:

            >>> project = toloka.Project(
            >>>     public_name='Cats vs dogs',
            >>>     public_description='A simple image classification',
            >>>     public_instructions='Determine which animal is in an image',
            >>>     ...
            >>> )
            >>> project.set_default_language('EN')
            >>> project.add_requester_translation(
            >>>     language='RU',
            >>>     public_name='Кошки или собаки'
            >>>     public_description='Простая классификация изображений'
            >>> )
            >>> project.add_requester_translation(language='RU', public_instructions='Определите, какое животное изображено')
        """
        assert language

        if self.localization_config is None:
            self.localization_config = LocalizationConfig()
        if self.localization_config.additional_languages is None:
            self.localization_config.additional_languages = []

        for translation in self.localization_config.additional_languages:
            if translation.language == language:
                current_translation = translation
                break
        else:
            current_translation = AdditionalLanguage(language=language)
            self.localization_config.additional_languages.append(current_translation)

        if public_name is not None:
            current_translation.public_name = AdditionalLanguage.FieldTranslation(value=public_name)
        if public_description is not None:
            current_translation.public_description = AdditionalLanguage.FieldTranslation(value=public_description)
        if public_instructions is not None:
            current_translation.public_instructions = AdditionalLanguage.FieldTranslation(value=public_instructions)
