-- SQL script that creates atrigger
CREATE TRIGGER decrease_qty AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
