# nagios-teams-alerts-integration
Integración para alertas con Nagios Core y MS Teams
# Nagios → Microsoft Teams Integration 🚀

Este repositorio contiene un script mejorado para integrar **Nagios Core** con **Microsoft Teams**, enviando notificaciones en tiempo real sobre el estado de tus hosts y servicios.

---

## ✨ Mejoras destacadas

✅ Emojis al inicio del título → identificación visual rápida (✅ UP, ❌ DOWN, ⚠️ WARNING)  
✅ Separación de notificaciones de host y servicio → comandos separados en `commands.cfg`  
✅ Script de prueba (`test-teams.sh`) → para enviar notificaciones manualmente  
✅ Compatible con cualquier canal de Teams

---

## 📖 Cómo instalarlo

1. Copia `notify-teams.py` a:
    ```bash
    /usr/local/nagios/libexec/
    ```
2. Asigna permisos:
    ```bash
    chmod +x /usr/local/nagios/libexec/notify-teams.py
    ```

3. Agrega a `commands.cfg`:
    ```bash
    define command {
        command_name notify_service_teams
        command_line /usr/local/nagios/libexec/notify-teams.py "$NOTIFICATIONTYPE$: $HOSTALIAS$/$SERVICEDESC$ → $SERVICESTATE$" "$SERVICEOUTPUT$" $_CONTACTWEBHOOKURL$
    }

    define command {
        command_name notify_host_teams
        command_line /usr/local/nagios/libexec/notify-teams.py "$NOTIFICATIONTYPE$: $HOSTALIAS$ → $HOSTSTATE$" "$HOSTOUTPUT$" $_CONTACTWEBHOOKURL$
    }
    ```

4. Configura `contacts.cfg` con tu webhook Teams.

5. Recarga Nagios:
    ```bash
    systemctl reload nagios
    ```

6. Prueba manualmente:
    ```bash
    ./test-teams.sh "PROBLEM: BD/MySQL → DOWN" "Servicio caído"
    ```

---

## 📷 Ejemplo visual

| Estado       | Ejemplo en Teams                         |
|--------------|-----------------------------------------|
| ✅ UP       | ✅ RECOVERY: BD/MySQL → OK         |
| ❌ DOWN     | ❌ PROBLEM: BD/MySQL → DOWN        |
| ⚠️ WARNING | ⚠️ PROBLEM: BD/MySQL → WARNING    |

---

## 🔗 Referencia original

Inspirado y extendido de: [isaac-galvan/nagios-teams-notify](https://github.com/isaac-galvan/nagios-teams-notify)
