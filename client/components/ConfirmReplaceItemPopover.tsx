/** @jsx jsx */

import * as React from 'react';
import { jsx, ClassNames } from '@emotion/core';
import Popover from 'antd/lib/popover';

import { item } from 'graphql/fragments/__generated__/item';
import { useTranslation } from 'i18n';
import { customSet } from 'graphql/fragments/__generated__/customSet';
import { itemBox, popoverTitleStyle } from 'common/mixins';
import ItemWithStats from './ItemWithStats';
import { useEquipItemMutation } from 'common/utils';

interface IProps {
  item: item;
  customSet: customSet;
  responsiveGridRef: React.MutableRefObject<HTMLDivElement | null>;
}

const ConfirmReplaceItemPopover: React.FC<IProps> = ({
  item,
  customSet,
  children,
  responsiveGridRef,
}) => {
  const { t } = useTranslation('common');
  const [selectedItemSlotId, setSelectedItemSlotId] = React.useState<
    string | null
  >(null);

  const [visible, setIsVisible] = React.useState(false);

  const mutate = useEquipItemMutation(item, customSet);

  const onSlotSelect = React.useCallback(
    async (e: React.MouseEvent<HTMLDivElement>) => {
      await mutate(e.currentTarget.dataset.slotId);
      setIsVisible(false);
    },
    [setSelectedItemSlotId, item, mutate, setIsVisible],
  );

  return (
    <ClassNames>
      {({ css }) => (
        <Popover
          getPopupContainer={() => responsiveGridRef.current || document.body}
          content={
            <div
              css={{
                width: '100%',
                display: 'flex',
                flexWrap: 'wrap',
                justifyContent: 'space-around',
                maxWidth: 240,
              }}
            >
              {customSet.equippedItems
                .filter(equippedItem =>
                  item.itemType.eligibleItemSlots
                    .map(slot => slot.id)
                    .includes(equippedItem.slot.id),
                )
                .sort((item1, item2) =>
                  item1.slot.id.localeCompare(item2.slot.id),
                )
                .map(equippedItem => (
                  <div
                    css={itemBox}
                    key={equippedItem.id}
                    data-slot-id={equippedItem.slot.id}
                    onClick={onSlotSelect}
                  >
                    <ItemWithStats
                      equippedItem={equippedItem}
                      selected={equippedItem.slot.id === selectedItemSlotId}
                      deletable={false}
                      customSet={customSet}
                    />
                  </div>
                ))}
            </div>
          }
          title={t('SELECT_ITEM_TO_REPLACE')}
          visible={visible}
          onVisibleChange={setIsVisible}
          trigger="click"
          overlayClassName={css(popoverTitleStyle)}
        >
          <div css={{ height: '100%' }}>{children}</div>
        </Popover>
      )}
    </ClassNames>
  );
};

export default ConfirmReplaceItemPopover;
