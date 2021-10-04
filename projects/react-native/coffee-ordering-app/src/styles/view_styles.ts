import {Dimensions, StyleSheet} from 'react-native';
import Colors from './colors';
const windowWidth = Dimensions.get('window').width;
const windowHeight = Dimensions.get('window').height;
const viewStyles = StyleSheet.create({
  mainView: {
    backgroundColor: Colors.white,
    flex: 1,
  },
  titleView: {
    margin: 16,
  },
  buttonView: {
    padding: 15,
    borderRadius: 10,
    alignItems: 'center',
    backgroundColor: Colors.lightGreen,
    marginVertical: 8,
    marginHorizontal: 20,
  },
  listView: {
    marginTop: 40,
    flex: 1,
    justifyContent: 'center',
  },
  ilusView: {
    marginTop: 40,
  },
  itemView: {
    alignItems: 'center',
    flexDirection: 'row',
    backgroundColor: Colors.darkGreen,
    marginHorizontal: 16,
    marginVertical: 8,
    borderRadius: 8,
    shadowColor: 'black',
  },
  circle: {
    width: 48,
    height: 46,
    margin: 24,
    borderRadius: 48 / 2,
    alignItems: 'center',
    justifyContent: 'flex-end',
    backgroundColor: Colors.deepGreen,
  },
  divider: {
    flex: 1,
    borderBottomColor: Colors.white,
    borderBottomWidth: 1,
    marginBottom: 12,
    marginHorizontal: 16,
  },
  imgStyle: {
    height: windowHeight / 3,
    width: windowWidth,
  },
  errorView: {
    flex: 1,
    justifyContent: 'flex-start',
    alignItems: 'center',
  },
});
export default viewStyles;
