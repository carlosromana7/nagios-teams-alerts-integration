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
### Preparar el webhook en Microsoft Teams

1. Abre **Microsoft Teams** y selecciona el canal donde quieres recibir las alertas.  
2. Haz clic en los **tres puntos (…) → Conectores**.  
3. Busca **Incoming Webhook** y haz clic en **Agregar**.  
4. Asigna un nombre (por ejemplo, `Nagios`) y opcionalmente sube un ícono.  
5. Haz clic en **Crear** → copia el enlace del webhook generado → guárdalo, lo necesitarás más adelante.

---

## 📖 Cómo instalarlo el plugin

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
vim /usr/local/nagios/etc/objects/contacts.cfg
define contact {
    contact_name                   teams-contact
    alias                          Microsoft Teams
    service_notification_commands  notify_service_teams
    host_notification_commands     notify_host_teams
    service_notification_options   w,u,c,r
    host_notification_options      d,u,r
    service_notification_period    24x7
    host_notification_period       24x7
    service_notification_interval  0
    host_notification_interval     0
    _CONTACTWEBHOOKURL             https://tu-webhook-de-teams
}

5.  Asociar contacto a un grupo (opcional)
Edita contactgroups.cfg:

define contactgroup {
    contactgroup_name       admins
    alias                  Nagios Administrators
    members                teams-contact
}
6. Recarga Nagios:
    ```bash
    systemctl reload nagios
    ```

7. Prueba manualmente:
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
