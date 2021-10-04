import React from 'react';
import {StyleSheet, Text, TouchableOpacity} from 'react-native';
import {Typography, ViewStyles} from '../styles';

export default function AppButton({
  title,
  onPress,
}: {
  onPress: any;
  title: string;
}) {
  return (
    <TouchableOpacity style={styles.buttonView} onPress={onPress}>
      <Text style={styles.buttonText}>{title}</Text>
    </TouchableOpacity>
  );
}
const styles = StyleSheet.create({
  buttonView: {
    ...ViewStyles.buttonView,
  },
  buttonText: {
    ...Typography.buttonText,
  },
});
