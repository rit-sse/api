<?php

use Illuminate\Database\Seeder;

class MemberTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        factory('App\Member', 50)->create()->each(function ($member) {
            $member->externalProfiles()
                ->save(factory('App\ExternalProfile')->make());
        });
    }
}
