// @ts-nocheck
import React from 'react';
import {Image, StyleSheet, Text, TouchableOpacity, View} from 'react-native';
import {Size} from '../models';
import {pickCoffeeSize} from '../redux/coffee_machine/coffee_machine_slice';
import {useAppDispatch} from '../redux/coffee_machine/hooks';
import {Typography, ViewStyles} from '../styles';
import {sizeAssets} from '../utils/constants';

export default function SizeCard({
  size,
  navigation,
}: {
  size: Size;
  navigation: any;
}) {
  const dispatch = useAppDispatch();

  return (
    <TouchableOpacity
      onPress={() => {
        dispatch(pickCoffeeSize(size));

        navigation.navigate('extra');
      }}>
      <View style={styles.itemView}>
        <View style={styles.circle}>
          <Image source={sizeAssets[size._id]} />
        </View>

        <Text style={styles.itemText}>{size.name}</Text>
      </View>
    </TouchableOpacity>
  );
}
const styles = StyleSheet.create({
  itemView: {
    ...ViewStyles.itemView,
  },
  circle: {
    ...ViewStyles.circle,
  },
  itemText: {
    ...Typography.itemText,
  },
});
