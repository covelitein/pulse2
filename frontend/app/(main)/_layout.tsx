import { Drawer } from 'expo-router/drawer';
import { GestureHandlerRootView } from 'react-native-gesture-handler';
import { View, Text, StyleSheet } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { palette, spacing, typography } from '../../constants/theme';
import { useAuthStore } from '../../store/authStore';
import { DrawerContentScrollView, DrawerItemList } from '@react-navigation/drawer';

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
    <GestureHandlerRootView style={{ flex: 1 }}>
      <Drawer
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
          name="home"
          options={{
            drawerLabel: 'Home',
            title: 'Home',
            drawerIcon: ({ color, size }) => (
              <Ionicons name="home" size={size} color={color} />
            ),
          }}
        />
        <Drawer.Screen
          name="habits"
          options={{
            drawerLabel: 'Habits',
            title: 'Habits',
            drawerIcon: ({ color, size }) => (
              <Ionicons name="checkmark-circle" size={size} color={color} />
            ),
          }}
        />
        <Drawer.Screen
          name="mood"
          options={{
            drawerLabel: 'Mood',
            title: 'Mood',
            drawerIcon: ({ color, size }) => (
              <Ionicons name="happy" size={size} color={color} />
            ),
          }}
        />
        <Drawer.Screen
          name="focus"
          options={{
            drawerLabel: 'Focus',
            title: 'Focus',
            drawerIcon: ({ color, size }) => (
              <Ionicons name="timer" size={size} color={color} />
            ),
          }}
        />
        <Drawer.Screen
          name="insights"
          options={{
            drawerLabel: 'Insights',
            title: 'Insights',
            drawerIcon: ({ color, size }) => (
              <Ionicons name="analytics" size={size} color={color} />
            ),
          }}
        />
        <Drawer.Screen
          name="search"
          options={{
            drawerLabel: 'Search',
            title: 'Search',
            drawerIcon: ({ color, size }) => (
              <Ionicons name="search" size={size} color={color} />
            ),
          }}
        />
        <Drawer.Screen
          name="notifications"
          options={{
            drawerLabel: 'Notifications',
            title: 'Notifications',
            drawerIcon: ({ color, size }) => (
              <Ionicons name="notifications" size={size} color={color} />
            ),
          }}
        />
        <Drawer.Screen
          name="profile"
          options={{
            drawerLabel: 'Profile',
            title: 'Profile',
            drawerIcon: ({ color, size }) => (
              <Ionicons name="person" size={size} color={color} />
            ),
          }}
        />
        <Drawer.Screen
          name="index"
          options={{
            drawerItemStyle: { display: 'none' },
          }}
        />
      </Drawer>
    </GestureHandlerRootView>
  );
}

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
