/**
 * Safe Mobile Haptic Vibration Helper
 */
export function triggerHaptic(type: 'light' | 'medium' | 'success' | 'warning' = 'light'): void {
  if (typeof window === 'undefined' || !('vibrate' in navigator)) return;
  try {
    switch (type) {
      case 'light':
        navigator.vibrate(10);
        break;
      case 'medium':
        navigator.vibrate(25);
        break;
      case 'success':
        navigator.vibrate([12, 30, 20]);
        break;
      case 'warning':
        navigator.vibrate([25, 40, 25]);
        break;
    }
  } catch {
    // Ignore environments where vibration permissions are restricted
  }
}
