package khaled.alaya.jwt_demo.controller;

import org.springframework.web.bind.annotation.RestController;

import khaled.alaya.jwt_demo.model.chat;
import khaled.alaya.jwt_demo.model.chatRequest;
import khaled.alaya.jwt_demo.service.chatService;
import khaled.alaya.jwt_demo.service.userJpaService;

import java.util.List;

import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.GetMapping;



@RestController
@RequestMapping("/api/chat")
public class chatController {


    private chatService chatService;
    private userJpaService userJpaService;

    public chatController(khaled.alaya.jwt_demo.service.chatService chatService,userJpaService userJpaService) {
        this.chatService = chatService;
        this.userJpaService=userJpaService;
    }


    @PostMapping()
    public chat addChat(@RequestBody chatRequest chatRequest){
        return chatService.addChat(chatRequest,userJpaService.loadUserByUsername(SecurityContextHolder.getContext().getAuthentication().getName()).getUsername());
    }

    @GetMapping("")
    public  List<chat> getAllChat() {
        return chatService.getAllChat(userJpaService.loadUserByUsername(SecurityContextHolder.getContext().getAuthentication().getName()).getUsername());
    }

}
