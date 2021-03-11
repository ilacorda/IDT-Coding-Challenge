package com.demo.controller;

import com.demo.exception.UserNotFoundException;
import com.demo.repository.UserRepository;
import com.demo.model.User;
import org.springframework.web.bind.annotation.*;

@RestController
public class UserController {

    private final UserRepository repository;

    public UserController(UserRepository repository) {
        this.repository = repository;
    }

    @GetMapping
    public Iterable returnAll() {
        return repository.findAll();
    }

    @GetMapping("/user/{id}")
    public User findOne(@PathVariable Long id) {
        return repository.findById(id)
                .orElseThrow(UserNotFoundException::new);
    }

    @PutMapping("/user/{id}")
    public User updateUser(@RequestBody User user, @PathVariable Long id) {
        if (user.getId() != id) {
            throw new UserNotFoundException();
        }
        repository.findById(id)
                .orElseThrow(UserNotFoundException::new);
        return repository.save(user);
    }
}
