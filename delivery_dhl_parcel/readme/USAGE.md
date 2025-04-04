Estas son las distintas operaciones posibles con este módulo:

## Grabar servicios

> 1.  Al confirmar el albarán, el servicio se grabará en DHL Parcel.
> 2.  Con la respuesta, se registrará en el chatter la referencia de
>     envío y las etiquetas correspondientes.
> 3.  Para gestionar los bultos del envío, se puede utilizar el campo de
>     número de bultos que añade delivery_package_number (ver el README
>     para mayor información) o bien el flujo nativo de Odoo con
>     paquetes de envío. El módulo mandará a la API de DHL Parcel el
>     número correspondiente y podremos descargar las etiquetas en PDF
>     con su correspondiente numeración.

## Cancelar servicios

> 1.  Al igual que en otros métodos de envío, en los albaranes de salida
>     podemos cancelar un servicio determinado mediante la acción
>     correspondiente en la pestaña de *Información Adicional*, sección
>     *Información de entrega* una vez el pedido esté confirmado y la
>     expedición generada.
> 2.  Podremos generar una nueva expedición una vez cancelado si fuese
>     necesario.

## Obtener etiquetas

> 1.  Si por error hubiésemos eliminado el adjunto de las etiquetas que
>     obtuvimos en la grabación del servicio, podemos obtenerlas de
>     nuevo pulsando en el botón "Etiqueta DHL Parcel" que tenemos en la
>     parte superior de la vista formulario del albarán.

## Seguimiento de envíos

> 1.  El módulo está integrado con delivery_state para poder recabar la
>     información de seguimiento de nuestros envíos directamente desde
>     la API de DHL Parcel.
> 2.  Para ello, vaya al albarán con un envío DHL Parcel ya grabado y en
>     la pestaña de *Información adicional* verá el botón *Actualizar
>     seguimiento* para pedir a la API que actualice el estado de este
>     envío en Odoo.

## Cierre del día

> 1.  Desde un smart button en el formulario del transportista, se puede
>     cerrar el día manualmente.

## Depuración de errores

> 1.  Es importante tener en cuenta que solo funcionará con códigos
>     postales de España (por lo menos para el consignatario).
> 2.  También puede activar Odoo con --log-level=debug para registrar
>     las peticiones y las respuestas en el log.

## Contrareembolso

> 1.  Al crear un envío con un método que tiene marcado el check de
>     contrareembolso, asumirá que hay un pedido vinculado al albarán y
>     usará el importe total del pedido como importe del
>     contrareembolso. Métodos de envío con este check no se encontrarán
>     disponibles en la web si se está usando.
