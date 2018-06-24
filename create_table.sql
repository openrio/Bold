CREATE TABLE `shopify_product_upsell`(
    `id` INT AUTO_INCREMENT NOT NULL,
    `author` VARCHAR(512),
    `body` LONGTEXT,
    `created_at` DATETIME,
    `shop_domain` VARCHAR(512),
    `shop_name` VARCHAR(512),
    `star_rating` INT,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB CHARACTER SET utf8;
