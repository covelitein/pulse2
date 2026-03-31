import React, { useEffect, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  Animated,
  TouchableOpacity,
  Dimensions,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { palette, spacing, borderRadius } from '../constants/theme';

interface ToastProps {
  message: string;
  type?: 'success' | 'error' | 'info';
  visible: boolean;
  onDismiss: () => void;
  duration?: number;
}

const { width } = Dimensions.get('window');

export default function Toast({
  message,
  type = 'info',
  visible,
  onDismiss,
  duration = 3000,
}: ToastProps) {
  const translateY = useRef(new Animated.Value(-100)).current;
  const timeoutRef = useRef<NodeJS.Timeout | null>(null);

  useEffect(() => {
    if (visible) {
      // Slide in
      Animated.spring(translateY, {
        toValue: 0,
        useNativeDriver: true,
        tension: 50,
        friction: 8,
      }).start();

      // Auto dismiss
      timeoutRef.current = setTimeout(() => {
        handleDismiss();
      }, duration);
    } else {
      // Slide out
      Animated.timing(translateY, {
        toValue: -100,
        duration: 200,
        useNativeDriver: true,
      }).start();
    }

    return () => {
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current);
      }
    };
  }, [visible]);

  const handleDismiss = () => {
    Animated.timing(translateY, {
      toValue: -100,
      duration: 200,
      useNativeDriver: true,
    }).start(() => {
      onDismiss();
    });
  };

  const getIconName = () => {
    switch (type) {
      case 'success':
        return 'checkmark-circle';
      case 'error':
        return 'close-circle';
      default:
        return 'information-circle';
    }
  };

  const getColor = () => {
    switch (type) {
      case 'success':
        return '#4ecdc4';
      case 'error':
        return '#ff6b6b';
      default:
        return palette.accentBlue;
    }
  };

  if (!visible && translateY._value === -100) {
    return null;
  }

  return (
    <Animated.View
      style={[
        styles.container,
        {
          transform: [{ translateY }],
        },
      ]}
    >
      <View style={[styles.toast, { borderLeftColor: getColor() }]}>
        <Ionicons name={getIconName() as any} size={24} color={getColor()} />
        <Text style={styles.message} numberOfLines={2}>
          {message}
        </Text>
        <TouchableOpacity onPress={handleDismiss} hitSlop={{ top: 10, bottom: 10, left: 10, right: 10 }}>
          <Ionicons name="close" size={20} color={palette.muted} />
        </TouchableOpacity>
      </View>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  container: {
    position: 'absolute',
    top: 50,
    left: spacing.md,
    right: spacing.md,
    zIndex: 9999,
  },
  toast: {
    backgroundColor: palette.surface,
    borderRadius: borderRadius.md,
    padding: spacing.md,
    flexDirection: 'row',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 8,
    borderLeftWidth: 4,
  },
  message: {
    flex: 1,
    color: palette.text,
    fontSize: 14,
    marginLeft: spacing.sm,
    marginRight: spacing.sm,
  },
});
