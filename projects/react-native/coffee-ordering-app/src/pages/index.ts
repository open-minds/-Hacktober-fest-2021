import {createStackNavigator, TransitionPresets} from 'react-navigation-stack';
import {createAppContainer} from 'react-navigation';
import ConnectScreen from './connect_page';
import StyleScreen from './style_page';
import SizeScreen from './size_screen';
import ExtraScreen from './extras_screen';
const screens = {
  connect: {
    screen: ConnectScreen,
    navigationOptions: {
      headerShown: false,
      ...TransitionPresets.ModalSlideFromBottomIOS,
    },
  },
  style: {
    screen: StyleScreen,
    navigationOptions: {
      headerShown: false,
      ...TransitionPresets.ModalSlideFromBottomIOS,
    },
  },
  size: {
    screen: SizeScreen,
    navigationOptions: {
      title: 'Brew with Lex',
      headerStyle: {
        elevation: 0,
      },
      ...TransitionPresets.ModalSlideFromBottomIOS,
    },
  },
  extra: {
    screen: ExtraScreen,
    navigationOptions: {
      title: 'Brew with Lex',
      headerStyle: {
        elevation: 0,
      },

      ...TransitionPresets.ModalSlideFromBottomIOS,
    },
  },
};
const AppStack = createStackNavigator(screens);
export default createAppContainer(AppStack);
