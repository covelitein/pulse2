import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { createDrawerNavigator, DrawerContentScrollView, DrawerItemList } from '@react-navigation/drawer';
import { NavigationContainer } from '@react-navigation/native';
import { palette, spacing, typography } from '../../constants/theme';
import { useAuthStore } from '../../store/authStore';
import HomeScreen from './home';
import HabitsScreen from './habits';
import MoodScreen from './mood';
import FocusScreen from './focus';
import InsightsScreen from './insights';
import SearchScreen from './search';
import NotificationsScreen from './notifications';
import ProfileScreen from './profile';
import { Ionicons } from '@expo/vector-icons';

const Drawer = createDrawerNavigator();

function CustomDrawerContent(props: any) {
  const { user } = useAuthStore();
  return (
    <DrawerContentScrollView {...props} style={styles.drawerContainer}>
      <View style={styles.drawerHeader}>
        <Ionicons name="pulse" size={40} color={palette.accentBlue} />
        <Text style={styles.drawerTitle}>Pulse</Text>
        <Text style={styles.drawerSubtitle}>{user?.name || 'User'}</Text>
        <Text style={styles.drawerEmail}>{user?.email || ''}</Text>
      </View>
      <DrawerItemList {...props} />
    </DrawerContentScrollView>
  );
}

export default function MainLayout() {
  return (
    <NavigationContainer independent={true}>
      <Drawer.Navigator
        drawerContent={(props) => <CustomDrawerContent {...props} />}
        screenOptions={{
          drawerStyle: {
            backgroundColor: palette.surface,
          },
          drawerActiveTintColor: palette.accentBlue,
          drawerInactiveTintColor: palette.muted,
          headerStyle: {
            backgroundColor: palette.surface,
          },
          headerTintColor: palette.text,
          headerShadowVisible: false,
        }}
      >
        <Drawer.Screen
          name="Home"
          component={HomeScreen}
          options={{
            drawerIcon: ({ color, size }) => (
              <Ionicons name="home" size={size} color={color} />
            ),
          }}
        />
        <Drawer.Screen
          name="Habits"
          component={HabitsScreen}
          options={{
            drawerIcon: ({ color, size }) => (
              <Ionicons name="checkmark-circle" size={size} color={color} />
            ),
          }}
        />
        <Drawer.Screen
          name="Mood"
          component={MoodScreen}
          options={{
            drawerIcon: ({ color, size }) => (
              <Ionicons name="happy" size={size} color={color} />
            ),
          }}
        />
        <Drawer.Screen
          name="Focus"
          component={FocusScreen}
          options={{
            drawerIcon: ({ color, size }) => (
              <Ionicons name="timer" size={size} color={color} />
            ),
          }}
        />
        <Drawer.Screen
          name="Insights"
          component={InsightsScreen}
          options={{
            drawerIcon: ({ color, size }) => (
              <Ionicons name="analytics" size={size} color={color} />
            ),
          }}
        />
        <Drawer.Screen
          name="Search"
          component={SearchScreen}
          options={{
            drawerIcon: ({ color, size }) => (
              <Ionicons name="search" size={size} color={color} />
            ),
          }}
        />
        <Drawer.Screen
          name="Notifications"
          component={NotificationsScreen}
          options={{


const styles = StyleSheet.create({
  drawerContainer: {
    backgroundColor: palette.surface,
  },
  drawerHeader: {
    padding: spacing.lg,
    paddingTop: spacing.xl,
    borderBottomWidth: 1,
    borderBottomColor: palette.border,
    marginBottom: spacing.md,
  },
  drawerTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: palette.text,
    marginTop: spacing.sm,
    fontFamily: typography.bold,
  },
  drawerSubtitle: {
    fontSize: 16,
    color: palette.text,
    marginTop: spacing.xs,
    fontFamily: typography.medium,
  },
  drawerEmail: {
    fontSize: 12,
    color: palette.muted,
    marginTop: spacing.xs / 2,
    fontFamily: typography.regular,
  },
});

            drawerIcon: ({ color, size }) => (
              <Ionicons name="notifications" size={size} color={color} />
            ),
          }}
        />
        <Drawer.Screen
          name="Profile"
          component={ProfileScreen}
          options={{
            drawerIcon: ({ color, size }) => (
              <Ionicons name="person" size={size} color={color} />
            ),
          }}
        />
      </Drawer.Navigator>
    </NavigationContainer>
  );
}
