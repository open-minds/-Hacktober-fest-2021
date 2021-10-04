import {StyleSheet, Text, View, FlatList, Image} from 'react-native';
import React, {useState} from 'react';
import Icon from 'react-native-vector-icons/FontAwesome';
// @ts-ignore
import {
  Collapse,
  CollapseHeader,
  CollapseBody,
  // @ts-ignore
} from 'accordion-collapse-react-native';
import {SubSelection} from '../models/subselection';
import {Colors, ViewStyles} from '../styles';
import {Extra} from '../models';
export default function ExtraCard({extra}: {extra: Extra}) {
  // const dispatch = useDispatch();
  const [pickedSubExtra, setpickedSubExtra] = useState(
    extra.subselections[0]._id,
  );
  const renderSubExtra = (subExtra: SubSelection) => {
    return (
      <View style={styles.subExtraView}>
        <Text style={styles.subExtraText}>{subExtra.name}</Text>
        <Icon
          style={styles.icon}
          onPress={() => {
            pickedSubExtra !== subExtra._id
              ? setpickedSubExtra(subExtra._id)
              : null;
          }}
          size={40}
          color={'white'}
          name={pickedSubExtra === subExtra._id ? 'check-circle-o' : 'circle-o'}
        />
      </View>
    );
  };

  return (
    <Collapse style={styles.itemView}>
      <CollapseHeader style={styles.collapseHeaderView}>
        <View style={styles.itemTitleView}>
          <View style={styles.circle}>
            <Image source={require('../assets/sizes/1.png')} />
          </View>
          <Text adjustsFontSizeToFit={true} style={styles.itemText}>
            {extra.name}
          </Text>
        </View>
      </CollapseHeader>
      <CollapseBody style={styles.collapseBodyView}>
        <View style={styles.divider} />
        <FlatList
          keyExtractor={element => element._id.toString()}
          data={extra.subselections}
          renderItem={({item}) => renderSubExtra(item)}
        />
      </CollapseBody>
    </Collapse>
  );
}
const styles = StyleSheet.create({
  //I did not write these styles in the styles folder because they are not used elsewhere in the app
  itemView: {
    backgroundColor: Colors.lightGreen,
    marginHorizontal: 16,
    marginVertical: 8,
    borderRadius: 8,
    shadowColor: 'black',
  },
  collapseHeaderView: {
    flexDirection: 'column',
  },
  collapseBodyView: {marginBottom: 24, flexDirection: 'column'},

  itemTitleView: {
    alignItems: 'center',
    flexDirection: 'row',
  },
  subExtraView: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    backgroundColor: Colors.darkGreen,
    marginVertical: 4,
    marginHorizontal: 24,
    borderRadius: 8,
  },
  subExtraText: {
    color: Colors.white,
    fontSize: 18,
    padding: 18,
  },
  icon: {
    padding: 10,
  },
  circle: {
    ...ViewStyles.circle,
  },
  divider: {
    ...ViewStyles.divider,
  },
  itemText: {
    color: Colors.white,
    fontSize: 18,
  },
});
