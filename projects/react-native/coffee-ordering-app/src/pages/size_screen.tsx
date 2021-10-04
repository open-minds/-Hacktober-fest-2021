import React from 'react';
import {StyleSheet, Text, View, FlatList} from 'react-native';
import {useAppSelector} from '../redux/coffee_machine/hooks';
import {CoffeeMachineSliceType} from '../redux/coffee_machine/coffee_machine_slice';
import SizeCard from '../components/size_card';
import {Typography, ViewStyles} from '../styles';

export default function SizeScreen({navigation}: {navigation: any}) {
  const state = useAppSelector((stat: CoffeeMachineSliceType) => stat);

  const sizes = state.pickedType.sizes;

  return (
    <View style={styles.mainView}>
      <View style={styles.titleView}>
        <Text style={styles.secondaryTitleText}>Select your size</Text>
      </View>
      <View style={styles.listView}>
        <FlatList
          keyExtractor={item => item._id.toString()}
          data={sizes}
          renderItem={({item}) => (
            <SizeCard size={item} navigation={navigation} />
          )}
        />
      </View>
    </View>
  );
}
const styles = StyleSheet.create({
  mainView: {
    ...ViewStyles.mainView,
  },
  titleView: {
    ...ViewStyles.titleView,
  },
  secondaryTitleText: {
    ...Typography.secondaryTitleText,
  },
  listView: {
    ...ViewStyles.listView,
  },
  titleText: {
    ...Typography.titleText,
  },
  itemView: {
    ...ViewStyles.itemView,
  },
  circle: {
    ...ViewStyles.circle,
  },
});
