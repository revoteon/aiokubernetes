# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.10.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401


from aiokubernetes.models.v1_label_selector import V1LabelSelector  # noqa: F401,E501


class V1alpha1AggregationRule(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cluster_role_selectors': 'list[V1LabelSelector]'
    }

    attribute_map = {
        'cluster_role_selectors': 'clusterRoleSelectors'
    }

    def __init__(self, cluster_role_selectors=None):  # noqa: E501
        """V1alpha1AggregationRule - a model defined in Swagger"""  # noqa: E501

        self._cluster_role_selectors = None
        self.discriminator = None

        if cluster_role_selectors is not None:
            self.cluster_role_selectors = cluster_role_selectors

    @property
    def cluster_role_selectors(self):
        """Gets the cluster_role_selectors of this V1alpha1AggregationRule.  # noqa: E501

        ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole's permissions will be added  # noqa: E501

        :return: The cluster_role_selectors of this V1alpha1AggregationRule.  # noqa: E501
        :rtype: list[V1LabelSelector]
        """
        return self._cluster_role_selectors

    @cluster_role_selectors.setter
    def cluster_role_selectors(self, cluster_role_selectors):
        """Sets the cluster_role_selectors of this V1alpha1AggregationRule.

        ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole's permissions will be added  # noqa: E501

        :param cluster_role_selectors: The cluster_role_selectors of this V1alpha1AggregationRule.  # noqa: E501
        :type: list[V1LabelSelector]
        """

        self._cluster_role_selectors = cluster_role_selectors

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.swagger_types.items():
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
        if not isinstance(other, V1alpha1AggregationRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
