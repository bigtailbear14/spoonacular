# coding: utf-8

"""
    spoonacular API

    The spoonacular Nutrition, Recipe, and Food API allows you to access over 380,000 recipes, thousands of ingredients, 800,000 food products, and 100,000 menu items. Our food ontology and semantic recipe search engine makes it possible to search for recipes using natural language queries, such as \"gluten free brownies without sugar\" or \"low fat vegan cupcakes.\" You can automatically calculate the nutritional information for any recipe, analyze recipe costs, visualize ingredient lists, find recipes for what's in your fridge, find recipes based on special diets, nutritional requirements, or favorite ingredients, classify recipes into types and cuisines, convert ingredient amounts, or even compute an entire meal plan. With our powerful API, you can create many kinds of food and especially nutrition apps.  Special diets/dietary requirements currently available include: vegan, vegetarian, pescetarian, gluten free, grain free, dairy free, high protein, whole 30, low sodium, low carb, Paleo, ketogenic, FODMAP, and Primal.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: mail@spoonacular.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse20010(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'ingredients': 'list[InlineResponse20010Ingredients]',
        'total_cost': 'float',
        'total_cost_per_serving': 'float'
    }

    attribute_map = {
        'ingredients': 'ingredients',
        'total_cost': 'totalCost',
        'total_cost_per_serving': 'totalCostPerServing'
    }

    def __init__(self, ingredients=None, total_cost=None, total_cost_per_serving=None):  # noqa: E501
        """InlineResponse20010 - a model defined in OpenAPI"""  # noqa: E501

        self._ingredients = None
        self._total_cost = None
        self._total_cost_per_serving = None
        self.discriminator = None

        self.ingredients = ingredients
        self.total_cost = total_cost
        self.total_cost_per_serving = total_cost_per_serving

    @property
    def ingredients(self):
        """Gets the ingredients of this InlineResponse20010.  # noqa: E501


        :return: The ingredients of this InlineResponse20010.  # noqa: E501
        :rtype: list[InlineResponse20010Ingredients]
        """
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        """Sets the ingredients of this InlineResponse20010.


        :param ingredients: The ingredients of this InlineResponse20010.  # noqa: E501
        :type: list[InlineResponse20010Ingredients]
        """
        if ingredients is None:
            raise ValueError("Invalid value for `ingredients`, must not be `None`")  # noqa: E501

        self._ingredients = ingredients

    @property
    def total_cost(self):
        """Gets the total_cost of this InlineResponse20010.  # noqa: E501


        :return: The total_cost of this InlineResponse20010.  # noqa: E501
        :rtype: float
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        """Sets the total_cost of this InlineResponse20010.


        :param total_cost: The total_cost of this InlineResponse20010.  # noqa: E501
        :type: float
        """
        if total_cost is None:
            raise ValueError("Invalid value for `total_cost`, must not be `None`")  # noqa: E501

        self._total_cost = total_cost

    @property
    def total_cost_per_serving(self):
        """Gets the total_cost_per_serving of this InlineResponse20010.  # noqa: E501


        :return: The total_cost_per_serving of this InlineResponse20010.  # noqa: E501
        :rtype: float
        """
        return self._total_cost_per_serving

    @total_cost_per_serving.setter
    def total_cost_per_serving(self, total_cost_per_serving):
        """Sets the total_cost_per_serving of this InlineResponse20010.


        :param total_cost_per_serving: The total_cost_per_serving of this InlineResponse20010.  # noqa: E501
        :type: float
        """
        if total_cost_per_serving is None:
            raise ValueError("Invalid value for `total_cost_per_serving`, must not be `None`")  # noqa: E501

        self._total_cost_per_serving = total_cost_per_serving

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse20010):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
